"""Utilities module for Fluxion.

This module provides various utility functions including:
- Model utilities
- Memory management
- Performance profiling
- Logging and monitoring
"""

# import safetensors
# import torch
from typing import Optional, Union, Dict, Any
# import logging
# import time
# from pathlib import Path


    
def check_device_compatibility(device: str):
    """ Checks the availability of gpus and nvdia-drivers
    
    Args:
        device: Device to check
    """
    
    def get_gpu_info_gpu_count_and_cuda_version():
        try:
            cuda_version = torch.version.cuda
            if torch.cuda.is_available():
                gpu_count = torch.cuda.device_count()
                gpu_names = [torch.cuda.get_device_name(i) for i in range(gpu_count)]
                return gpu_count, gpu_names, cuda_version
            else:
                return 0, None, cuda_version
        except Exception as e:
            logger.error(f"Error checking cuda version: {e}")
            return None, None, None
    
    gpu_count, gpu_names, cuda_version = get_gpu_info_gpu_count_and_cuda_version()
    if gpu_count > 0:
        logger.info(f"Found {gpu_count} GPUs: {gpu_names}")
        logger.info(f"CUDA version: {cuda_version}")
        return True
    else:
        logger.error("No GPUs found. Please check your GPU configuration.")
    return False
    
    

class Timer:
    """Simple timer for performance measurements."""
    
    def __init__(self, name: str):
        """Initialize timer.
        
        Args:
            name: Timer name for identification
        """
        self.name = name
        self.start_time: Optional[float] = None
        
    def __enter__(self) -> 'Timer':
        self.start_time = time.perf_counter()
        return self
        
    def __exit__(self, *args: Any) -> None:
        if self.start_time is None:
            return
        elapsed = time.perf_counter() - self.start_time
        logging.info(f"{self.name} took {elapsed:.4f} seconds")
        
class ModelLoader:
    """Torch and Safetensors Model Loader"""
    
    def __init__(self, model_path: str, loader_type: str = "safetensors", device: str = "cpu"):
        self.model_path = model_path
        self.loader_type = loader_type
        self.device = device
        
    def load_model(self):
        if loader_type == "torch":
            self.model = torch.load(model_path)
        elif loader_type == "safetensors":
            self.model = safetensors.load_model(model_path)
        
        
        

        
