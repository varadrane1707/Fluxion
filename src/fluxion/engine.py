
from asyncio.log import logger
from fluxion.utils.context_managers import ModelManager,PipelineManager
from fluxion.utils.config import ServerConfig

from fluxion.modules.downloaders.base import ModelDownloader

class FluxionEngine():
    def __init__(self, config: ServerConfig):
        logger.info(f"Initializing Fluxion Engine with config: {config}")
        self.config = config
        self.model_manager = ModelManager.register(model_name=self.config.model_name,model_source_type=self.config.model_source_type,model_source_path=self.config.model_source_path,model_format=self.config.model_format)
        self.download_model_to_local()
        self.device = self.config.device
        self.base_components = {}
        
    def download_model_to_local(self):
        downloader = ModelDownloader()
        downloader.maybe_download_model()
        return 
    
    def load_and_get_base_components(self):
        self.base_components = None
        logger.info(f"Base components loaded: {self.base_components}")
        return self.base_components
        
        
        
        