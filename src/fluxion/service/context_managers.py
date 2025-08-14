import os
from typing import Any
from ..utils.constants import LORA_LRU_CACHE_MAX_SIZE,CONTROLNET_LRU_CACHE_MAX_SIZE,CACHE_DIR
from .lru_cache import LRUCache

class BaseContextManager:
    def __init__(self):
        self.context = None
        
    def get_context(self):
        return self.context
    
    def register_context(self,context:Any):
        self.context = context


class ModelManager(BaseContextManager):
    def __init__(self):
        self.model_dir = os.getenv("MODEL_DIR","/models/")
        self.model_dict = {}
        
    def get_model_dict(self):
        return self.model_dict

class PipelineManager():
    def __init__


class LoraManager():
    def __init__(self, lora_path: str):
        self.lora_dir = os.path.join(CACHE_DIR, "lora/")
        self.lru_cache = LRUCache(LORA_LRU_CACHE_MAX_SIZE)
        
    def get_lora(self,lora_path:str):
        if lora_path in self.lru_cache:
            return self.lru_cache.get(lora_path)
        else:
            lora_path = os.path.join(self.lora_dir, lora_path)
            if os.path.exists(lora_path):
                self.lru_cache.put(lora_path, lora_path)
                return lora_path
            else:
                raise FileNotFoundError(f"Lora file {lora_path} not found")
    