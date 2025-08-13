from typing import Any,OrderedDict

class LRUCache:
    def __init__(self, max_size: int):
        self.cache = OrderedDict()
        self.max_size = max_size
        
    def get(self, key: str):
        if key not in self.cache:
            raise KeyError(f"Key {key} not found in cache")
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: str, value: Any):
        if key in self.cache:
            self.cache.move_to_end(key)
        if len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
    def clear(self):
        self.cache.clear()
        
    def remove(self, key: str):
        self.cache.pop(key)
        
    def __len__(self):
        return len(self.cache)
    
class DiskCache:
    def __init__(self, cache_dir: str,max_size:int,max_disk_size:int):
        self.cache_dir = cache_dir
        self.cache = OrderedDict()
        self.max_size = max_size
        self.max_disk_size = max_disk_size

                
    def get(self, key: str):
        if key not in self.cache:
            raise KeyError(f"Key {key} not found in cache")
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: str, value: Any):
        if key in self.cache:
            self.cache.move_to_end(key)
        if len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
    def clear(self):
        self.cache.clear()
        
    def remove(self, key: str):
        self.cache.pop(key)
        
    def __len__(self):
        return len(self.cache)