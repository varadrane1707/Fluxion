from .base_zmq import BaseWorker

class PreprocessorWorker(BaseWorker):
    """
    Preprocessor worker is responsible for preprocessing the data before it is sent to the model.
    Downloads the images,loras,controlnets,etc.
    
    Args:
        BaseWorker: Base worker class
        
    Returns:
        dict: Preprocessed data
        
    Raises:
        Exception: If the data is not valid
        
    Attributes:
        logger: Logger for the worker
        context: ZMQ context
        socket: ZMQ socket
    """
    
    
    
    def process(self, data: dict) -> dict:
        