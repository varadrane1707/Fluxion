import asyncio
import threading
import queue
from typing import Optional, Callable
from ..validations.dataclasses import Text2ImgRequestData, Img2ImgRequestData, InpaintingRequestData
from .download import download_image
from fastapi import HTTPException
from loguru import logger
import uuid
from concurrent.futures import ThreadPoolExecutor

class ValidationResult:
    def __init__(self,request_id: str,data: dict,error: Optional[str] = None,success: bool = True
                 ):
        self.request_id = request_id
        self.result = data
        self.error = error
        self.success = success
        
class ValidatorQueue:
    def __init__(self,max_size: int = 1000):
        self.queue = queue.Queue(maxsize=max_size)
        self.results = {}
        self.callbacks = {}
    
    def put_request(self,data: dict,callback: callable = None):
        request_id = data.get('request_id',str(uuid.uuid4()))
        if callback:
            self.callbacks[request_id] = callback
        try:
            self.queue.put(data)
        except queue.Full:
            raise HTTPException(status_code=429, detail="Queue is full")
        
    def get_request(self, timeout: float = 1.0) -> Optional[dict]:
        """Get a validation request from the queue"""
        try:
            return self.queue.get(timeout=timeout)
        except queue.Empty:
            return None
        
    def put_result(self,result: ValidationResult):
        """Store validation result"""
        self.results[result.request_id] = result
        request_id = result.request_id
        # Execute callback if provided
        if request_id in self.callbacks:
            try:
                self.callbacks[request_id](result)
            except Exception as e:
                logger.error(f"Callback error for request {request_id}: {str(e)}")
            finally:
                del self.callbacks[request_id]
    
    def get_result(self, request_id: str, timeout: float = 30.0) -> Optional[ValidationResult]:
        """Get validation result by request_id"""
        start_time = asyncio.get_event_loop().time()
        
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            if request_id in self.results:
                result = self.results.pop(request_id)
                return result
            asyncio.sleep(0.1)
        
        return None
        
class ValidatorWorker():
    def __init__(self,num_workers: int = 4):
        self.num_workers = num_workers
        self.is_running = False
        self.queue = ValidatorQueue()
        self.workers = []
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        
    def start(self):
        self.is_running = True
        logger.info(f"Starting {self.num_workers} validator workers")
        
        for i in range(self.num_workers):
            worker_ = threading.Thread(target=self._worker_loop,args=(i,))
            worker_.daemon = True
            worker_.start()
            self.workers.append(worker_)
            
    def stop(self):
        self.is_running = False
        logger.info(f"Stopping {self.num_workers} validator workers")
        for worker in self.workers:
            worker.join()
        self.executor.shutdown(wait=True)
        logger.info(f"Validator workers stopped")
        
    def _worker_loop(self,worker_id: int):
        logger.info(f"Validator worker {worker_id} started")
        while self.is_running:
            try:
                request = self.queue.get_request()
            except Exception as e:
                logger.error(f"Validator worker {worker_id} error: {str(e)}")
                continue
            
    def _process_request(self,request: dict,worker_id: int):
        request_id = request.get('request_id',str(uuid.uuid4()))
        try:
            validated_data = self.validate(request)
            self.queue.put_result(ValidationResult(request_id,validated_data))
        except Exception as e:
            logger.error(f"Validator worker {worker_id} error: {str(e)}")
            self.queue.put_result(ValidationResult(request_id,request,error=str(e),success=False))
            
    def validate(self, data: dict):
        """Validate request data based on model type"""
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")
            
        model_type = data.get('model_type')
        if not model_type:
            raise ValueError("model_type is required")
        
        try:
            if model_type == 'text2img':
                return Text2ImgRequestData(**data)
            elif model_type == 'img2img':
                return Img2ImgRequestData(**data)
            elif model_type == 'inpainting':
                return InpaintingRequestData(**data)
            else:
                raise ValueError(f"Invalid model type: {model_type}")
                
        except TypeError as e:
            raise ValueError(f"Invalid parameters for {model_type}: {str(e)}")
        
    async def put_request_async(self, data: dict, callback: Optional[Callable] = None) -> str:
        """Async wrapper for putting requests"""
        return await asyncio.get_event_loop().run_in_executor(
            self.executor, 
            self.queue.put_request, 
            data, 
            callback
        )
    
    async def get_result_async(self, request_id: str, timeout: float = 30.0) -> Optional[ValidationResult]:
        """Async wrapper for getting results"""
        return await asyncio.get_event_loop().run_in_executor(
            self.executor, 
            self.queue.get_result, 
            request_id, 
            timeout
        )
    
    def put_request_sync(self, data: dict, callback: Optional[Callable] = None) -> str:
        """Synchronous method to put request"""
        return self.queue.put_request(data, callback)
    
    def get_result_sync(self, request_id: str, timeout: float = 30.0) -> Optional[ValidationResult]:
        """Synchronous method to get result"""
        import time
        start_time = time.time()
        
        while (time.time() - start_time) < timeout:
            if request_id in self.queue.results:
                return self.queue.results.pop(request_id)
            time.sleep(0.1)
        return None
        
        
        