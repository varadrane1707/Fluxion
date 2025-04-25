import torch
from PIL import Image


class FluxTxt2ImgPipeline():
    """
    docstring:
    Usage:

    from Fluxion.pipelines.models.flux_txt2img import FluxTxt2ImgPipeline
    pipeline = FluxTxt2ImgPipeline(
        vae=vae,
        unet=unet,
        scheduler=scheduler,
        tokenizer=tokenizer,
        text_encoder=text_encoder,
    )
    """
    
    def __init__(self, 
                 vae, 
                 unet, 
                 scheduler, 
                 tokenizer, 
                 text_encoder, 
                 tokenizer2, 
                 text_encoder2):
        self.vae = vae
        self.unet = unet
        self.scheduler = scheduler
        self.tokenizer = tokenizer
        self.text_encoder = text_encoder
        self.tokenizer2 = tokenizer2
        self.text_encoder2 = text_encoder2
        
        
    def __call__(self, 
                 prompt: str, 
                 num_inference_steps: int = 50, 
                 guidance_scale: float = 7.5, 
                 num_images_per_prompt: int = 1, 
                 num_inference_steps_2: int = 50, 
                 guidance_scale_2: float = 7.5, 
                 num_images_per_prompt_2: int = 1,):
        pass 
        
