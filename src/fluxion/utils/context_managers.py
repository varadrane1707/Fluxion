import os
from typing import Any
from .constants import LORA_LRU_CACHE_MAX_SIZE,CONTROLNET_LRU_CACHE_MAX_SIZE,CACHE_DIR
from ..service.lru_cache import LRUCache
from loguru import logger

class ModelManager():
    def __init__(self):
        self.model_dir = None
        self.model_dict = {}
        
    def get_model_dict(self):
        if not self.model_dict:
            logger.error("Model dictionary is empty")
            raise ValueError("Model dictionary is empty")
        return self.model_dict
    
    def register(self,model_name:str,model_source_type:str,model_source_path:str,model_format:str):
        self.model_dict[model_name] = {
            "model_source_type": model_source_type,
            "model_source_path": model_source_path,
            "model_format": model_format
        }
        return self.model_dict[model_name]

class PipelineManager():
    def __init__(self):
        self.pipeline_dict = {}
        
    def get_pipeline_dict(self):
        if not self.pipeline_dict:
            logger.error("Pipeline dictionary is empty")
            raise ValueError("Pipeline dictionary is empty")
        return self.pipeline_dict
    
    def register(self,pipeline_type:[list[str]],pipeline_config:dict):
        self.pipeline_dict[pipeline_type] = pipeline_config
        self.pipeline_dict[pipeline_config] = pipeline_config
        return self.pipeline_dict


    