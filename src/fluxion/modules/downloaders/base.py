
from loguru import logger
from ...utils.context_managers import ModelManager


class ModelDownloader():
    """
    This class is used to download the model to the local directory.
    """      
    def __init__(self):
        pass
        
    def maybe_download_model(self):
        model_dict= ModelManager.get_model_dict()
        if model_dict is {}:
            logger.error("Model dictionary is empty")
            raise ValueError("Model dictionary is empty")
        
        model_name = model_dict['model_name']

        if model_name.lower() == "flux":
            from .flux import FluxModelDownloader
            model_downloader = FluxModelDownloader()  
        else:
            logger.error(f"Model loader for {model_name} is not implemented")
            raise NotImplementedError(f"Model loader for {model_name} is not implemented")
        return model_downloader.download_model_to_local()
        