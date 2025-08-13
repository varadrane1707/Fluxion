import torch
from fluxion.models.transformers.transformer_flux import FluxTransformerModel
from fluxion.utils.config import OptimisationConfig

from diffusers import DiffusionPipeline,AutoencoderKL
from transformers import CLIPTokenizer, T5TokenizerFast, CLIPTextModel, T5EncoderModel

class FluxBasePipeline(DiffusionPipeline):
    def __init__(self,optims: OptimisationConfig):
        self.optims = optims
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
          
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Base Pipeline is not callable.")
    
    def load_vae(self, vae_path: str):
        vae = AutoencoderKL.from_pretrained(vae_path).to(self.device)
        return vae
    
    def load_transformer(self, transformer_path: str):
        transformer = FluxTransformerModel.from_pretrained(transformer_path).to(self.device)
        return transformer
    
    def load_text_encoder_1(self, text_encoder_path: str):
        text_encoder_1 = CLIPTextModel.from_pretrained(text_encoder_path).to(self.device)
        return text_encoder_1
    
    def load_text_encoder_2(self, text_encoder_path: str):
        text_encoder_2 = T5EncoderModel.from_pretrained(text_encoder_path).to(self.device)
        return text_encoder_2
    
    def load_tokenizer_1(self, tokenizer_path: str):
        tokenizer_1 = CLIPTokenizer.from_pretrained(tokenizer_path)
        return tokenizer_1
    
    def load_tokenizer_2(self, tokenizer_path: str):
        tokenizer_2 = T5TokenizerFast.from_pretrained(tokenizer_path)
        return tokenizer_2
    
    def load_from_single_file(self, file_path: str):
        pass
    
    
    
    
    
    
    
    
        
        
        