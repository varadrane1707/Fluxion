"Caches registry for the context managers"

from typing import Any

class BaseRegistry:
    def __init__(self):
        self.registry = {}
        
    def register(self,name:str):
        self.registry[name] = name
        
    def get(self,name:str):
        return self.registry[name]
    
    def __len__(self):
        return len(self.registry)
    
    def __iter__(self):
        return iter(self.registry)
    
    def __contains__(self,name:str):
        return name in self.registry
    
    def __getitem__(self,name:str):
        return self.registry[name]
    
    def __setitem__(self,name:str,context_manager:Any):
        self.registry[name] = context_manager
        
    def __delitem__(self,name:str):
        del self.registry[name]
        
class ModelRegistry(BaseRegistry):
    def __init__(self):
        super().__init__()
        
    def register_model(self,name:str):
        self.registry[name] = name
        
    def get_model(self,name:str):
        return self.registry[name]
    
class PipelineRegistry(BaseRegistry):
    def __init__(self):
        super().__init__()
        
    def register_pipeline(self,pipeline_type:str):
        self.registry[pipeline_type] = pipeline_type
        
    def get_pipeline(self,pipeline_type:str):
        return self.registry[pipeline_type]
    
    
        