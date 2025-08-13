from loguru import logger
import traceback



def FluxionLogger(message: str,method: str):    
    def log_info(message: str):
        logger.info(message)
        
    def log_error(message: str):
        logger.error(message)
        
    def log_warning(message: str):
        logger.warning(message)
        
    def log_debug(message: str):
        logger.debug(message)
        
    def log_trace():
        logger.trace(traceback.format_exc())
      
    method = method.lower()
    if method == "info":
        log_info(message)
    elif method == "error":
        log_error(message)
    elif method == "warning":
        log_warning(message)
    elif method == "debug":
        log_debug(message)
    elif method == "trace":
        log_trace()