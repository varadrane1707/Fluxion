from dataclasses import dataclass
from typing import List, Optional


def validate_data(data: dict):
    if data['model_type'] == 'text2img':
        validated_data = Text2ImgRequestData(**data)
    elif data['model_type'] == 'img2img':
        validated_data = Img2ImgRequestData(**data)
    elif data['model_type'] == 'inpainting':
        validated_data = InpaintingRequestData(**data)
    else:
        raise ValueError(f"Invalid model type: {data.get('model_type','None')}")
    
    return to_dict(validated_data)

def to_dict(class_instance):
    return {
        key: value for key, value in class_instance.__dict__.items()
    }
    
@dataclass
class Text2ImgRequestData:
    prompt: str = None
    prompt2: str = None
    negative_prompt: str = None
    negative_prompt2: str = None
    num_inference_steps: int = 28
    num_images_per_prompt: int = 1
    seed: int = -1
    guidance_scale: float = 7.5
    width: int = 1024
    height: int = 1024
    pipeline_type: List[str] = ['text2img']
    loras: Optional[List[str]]
    
    def __post_init__(self):
        self.pipeline_type = ['text2img']
        
    def from_dict(self,data: dict):
        self.prompt = data['prompt']
        self.prompt2 = data['prompt2']
        self.negative_prompt = data['negative_prompt']
        self.negative_prompt2 = data['negative_prompt2']
        self.num_inference_steps = data['num_inference_steps']
        return self
        
        
    
    

@dataclass
class Img2ImgRequestData:
    image: str = None
    prompt: str = None
    prompt2: str = None
    negative_prompt: str = None
    negative_prompt2: str = None
    num_inference_steps: int = 28
    num_images_per_prompt: int = 1
    seed: int = -1
    guidance_scale: float = 7.5
    strength: float = 0.75
    width: int = 1024
    height: int = 1024
    pipeline_type: List[str] = ['img2img']
    loras: Optional[List[str]] = None
    
@dataclass
class InpaintingRequestData:
    image: str = None
    prompt: str = None
    prompt2: str = None
    negative_prompt: str = None
    negative_prompt2: str = None
    num_inference_steps: int = 28
    num_images_per_prompt: int = 1
    seed: int = -1
    guidance_scale: float = 7.5
    strength: float = 0.75
    width: int = 1024
    height: int = 1024
    pipeline_type: List[str] = ['inpainting']
    loras: Optional[List[str]] = None
    
    def from_dict(self,data: dict):
        self.image = data['image']
        self.prompt = data['prompt']
        self.prompt2 = data['prompt2']
        self.negative_prompt = data['negative_prompt']
        self.negative_prompt2 = data['negative_prompt2']
        return self

    
    