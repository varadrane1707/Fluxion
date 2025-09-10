from typing import Any

class BaseRegistry:
    def __init__(self):
        self.registry = {}
        
    def register(self, name, value):
        self.registry[name] = value
        
    def get(self, name):
        return self.registry[name]
    
    
class ModelRegistry(BaseRegistry):
    def __init__(self):
        super().__init__()
        
    def register_model(self, name, model):
        self.registry[name] = model
        
    def get_model(self, name):
        return self.registry[name]
    
class PipelineRegistry(BaseRegistry):
    
    def register_pipeline_config(self, name, pipeline_config):
        self.registry[name] = pipeline_config
        
    def get_pipeline_config(self, name):
        return self.registry[name]
    
    def register_pipeline(self, name, pipeline):
        self.registry[name] = pipeline
        
    def get_pipeline(self, name):
        return self.registry[name]
    
    def register_pipeline_type(self, name, pipeline_type):
        self.registry[name] = pipeline_type
        

        