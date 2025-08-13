import os
from ..utils.constants import LORA_LRU_CACHE_MAX_SIZE,CONTROLNET_LRU_CACHE_MAX_SIZE,CACHE_DIR
from .lru_cache import LRUCache


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
    