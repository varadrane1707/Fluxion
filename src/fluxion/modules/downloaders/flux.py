from loguru import logger
import torch
import os
from ...utils.context_managers import ModelManager
from ...utils.constants import MODEL_CACHE_DIR

from huggingface_hub import snapshot_download

class FluxModelDownloader():
    """
    This class is used to download the Flux model to the local directory.
    """
    def __init__(self):
        self.model_dict = ModelManager.get_model_dict()
        if self.model_dict is {}:
            logger.error("Model dictionary is empty")
            raise ValueError("Model dictionary is empty")
        
        self.model_path = self.model_dict['model_source_path']
        self.device = self.model_dict['device']
        self.model_format = self.model_dict['model_format']
        self.model_name = self.model_dict['model_name']
        self.model_source_type = self.model_dict['model_source_type']
        self.local_dir = MODEL_CACHE_DIR
        
    def download_model_to_local(self):
        if self.model_source_type.lower() == "huggingface":
            logger.info(f"Downloading model from HuggingFace to local directory: {self.local_dir}")
            if os.getenv("HF_TOKEN") is not None:
                snapshot_download(self.model_path, local_dir=self.local_dir, token=os.getenv("HF_TOKEN"))
            else:
                raise ValueError("HF_TOKEN is not set. Flux is a private model and requires a token to download.")

        elif self.model_source_type.lower() == "local":
            if self.model_path == MODEL_CACHE_DIR and os.path.isdir(self.model_path):
                self.local_dir = MODEL_CACHE_DIR
            else:
                self.local_dir = self.model_path
        elif self.model_source_type.lower() == "zip_url":
            raise NotImplementedError("Zip URL model source type is not supported") 
        else:
            logger.error(f"Model source type {self.model_source_type} is not supported")
            raise NotImplementedError(f"Model source type {self.model_source_type} is not supported")

        