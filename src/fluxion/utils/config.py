from dataclasses import dataclass, field
import json
import os
from typing import Optional, List
from enum import Enum
from ._log import FluxionLogger
import yaml

@dataclass
class AvailableAttentionBackends(Enum):
    FAST_ATTENTION = "FastAttention"
    FLASH_ATTENTION = "FlashAttention"

    @classmethod
    def from_str(cls, attention_backend: str):
        if attention_backend == "fast_attention":
            return cls.FAST_ATTENTION
        elif attention_backend == "flash_attention":
            return cls.FLASH_ATTENTION
        else:
            raise ValueError(f"Invalid attention backend: {attention_backend}")
    
@dataclass
class AvailableQuantization(Enum):
    FP8 = "FP8"
    NONE = "None"

    @classmethod
    def from_str(cls, quantization: str):
        if quantization.lower() == "fp8":
            return cls.FP8
        elif quantization.lower() == "none":
            return cls.NONE
        else:
            raise ValueError(f"Invalid quantization: {quantization}")
        
@dataclass
class PipelineConfig:
    use_controlnet: bool = False
    use_multicontrolnet: bool = False
    
    @classmethod
    def from_dict(cls, pipeline_config: dict):
        # Handle empty dict or missing keys by using defaults
        if not pipeline_config:
            return cls()
        
        use_controlnet = pipeline_config.get("use_controlnet", False)
        use_multicontrolnet = pipeline_config.get("use_multicontrolnet", False)
        
        return cls(
            use_controlnet=use_controlnet,
            use_multicontrolnet=use_multicontrolnet
        )
        
class Model``
    
@dataclass
class AvailableCaching(Enum):
    FBCACHE = "FBCache"
    NONE = "None"

    @classmethod
    def from_str(cls, caching: str):
        if caching.lower() == "fbcache":
            return cls.FBCACHE
        elif caching.lower() == "none":
            return cls.NONE
        else:
            raise ValueError(f"Invalid caching: {caching}")
    
@dataclass
class AvailableCompilation(Enum):
    SimpliCompile = "SimpliCompile"
    TorchCompile = "TorchCompile"
    NONE = "None"
    
    @classmethod
    def from_str(cls, compilation: str):
        if compilation.lower() == "simpli_compile":
            return cls.SimpliCompile
        elif compilation.lower() == "torch_compile":
            return cls.TorchCompile
        elif compilation.lower() == "none":
            return cls.NONE
        else:
            raise ValueError(f"Invalid compilation: {compilation}")
    
@dataclass
class AvailableModelSourceType(Enum):
    HuggingFace = "huggingface"
    Local = "local"
    ZIP_URL = "zip_url"
    
    @classmethod
    def from_str(cls, model_source_type: str):
        if model_source_type.lower() == "huggingface":
            return cls.HuggingFace
        elif model_source_type.lower() == "local":
            return cls.Local
        elif model_source_type.lower() == "zip_url":
            return cls.ZIP_URL
        else:
            raise ValueError(f"Invalid model source type: {model_source_type}")
        
@dataclass
class AvailableModelFormat(Enum):
    Diffusers = "diffusers"
    Safetensors = "safetensors"
    
    @classmethod
    def from_str(cls, model_format: str):
        if model_format.lower() == "diffusers":
            return cls.Diffusers
        elif model_format.lower() == "safetensors":
            return cls.Safetensors
        else:
            raise ValueError(f"Invalid model format: {model_format}")
        
@dataclass
class AvailablePipelineType(Enum):
    Txt2Img = "txt2img"
    Img2Img = "img2img"
    Inpainting = "inpainting"
    Txt2Img_Controlnet = "txt2img_controlnet"
    Img2Img_Controlnet = "img2img_controlnet"
    Inpainting_Controlnet = "inpainting_controlnet"
    Txt2Img_Multicontrolnet = "txt2img_multicontrolnet"
    Img2Img_Multicontrolnet = "img2img_multicontrolnet"
    Inpainting_Multicontrolnet = "inpainting_multicontrolnet"
    Custom = "custom"
    
    @classmethod
    def from_list(cls, pipeline_types: List[str]):
        return [cls(pipeline_type) for pipeline_type in pipeline_types]
    
@dataclass
class AvailableDevice(Enum):
    CPU = "cpu"
    GPU = "cuda"
    
    @classmethod
    def from_str(cls, device: str):
        if device.lower() == "cpu":
            return cls.CPU
        elif device.lower() == "cuda":
            return cls.GPU
        else:
            raise ValueError(f"Invalid device: {device}")
    
@dataclass
class AvailableDtype(Enum):
    BFloat16 = "bf16"
    Float16 = "fp16"
    
    @classmethod
    def from_str(cls, dtype: str):
        if dtype.lower() == "bf16":
            return cls.BFloat16
        elif dtype.lower() == "fp16":
            return cls.Float16
        else:
            raise ValueError(f"Invalid dtype: {dtype}")
        
@dataclass
class ServerConfig():
    """
    Example config : 
    
    {
    "model_source_type": "HuggingFace",
    "model_source_path": "black-forest-labs/FLUX.1-dev",
    "model_format": "Safetensors",
    "pipeline_type": ["Txt2Img", "Img2Img", "Inpainting"],
    "pipeline_config": {
        "use_controlnet": False,
        "use_multicontrolnet": False
    },
    "device": "cuda",
    "dtype": "bf16",
    "attention_backend": "flash_attention_2",
    "quantization": "FP8",
    "use_caching": "FBCache",
    "compile": "None"  # SimpliCompile, TorchCompile, None
    }
    
    """
    model_source_type: Optional[AvailableModelSourceType] = AvailableModelSourceType.HuggingFace
    model_source_path: Optional[str] = "black-forest-labs/FLUX.1-dev"
    model_format: Optional[AvailableModelFormat] = AvailableModelFormat.Diffusers
    pipeline_type: Optional[List[AvailablePipelineType]] = field(default_factory=lambda: [AvailablePipelineType.Txt2Img])
    pipeline_config: Optional[PipelineConfig] = field(default_factory=PipelineConfig)
    device: Optional[AvailableDevice] = AvailableDevice.GPU
    dtype: Optional[AvailableDtype] = AvailableDtype.BFloat16
    attention_backend: Optional[AvailableAttentionBackends] = AvailableAttentionBackends.FAST_ATTENTION
    caching: Optional[AvailableCaching] = AvailableCaching.FBCACHE
    compilation: Optional[AvailableCompilation] = AvailableCompilation.NONE
    quantization: Optional[AvailableQuantization] = AvailableQuantization.FP8
    
    def __repr__(self):
        """Custom repr to show enum values instead of enum objects"""
        return (
            f"ServerConfig(\n"
            f"  model_source_type='{self.model_source_type.value}',\n"
            f"  model_source_path='{self.model_source_path}',\n"
            f"  model_format='{self.model_format.value}',\n"
            f"  pipeline_type={[pt.value for pt in self.pipeline_type]},\n"
            f"  pipeline_config={self.pipeline_config},\n"
            f"  device='{self.device.value}',\n"
            f"  dtype='{self.dtype.value}',\n"
            f"  attention_backend='{self.attention_backend.value}',\n"
            f"  caching='{self.caching.value}',\n"
            f"  compilation='{self.compilation.value}',\n"
            f"  quantization='{self.quantization.value}'\n"
            f")"
        )
    
    def __post_init__(self):
        if self.model_source_type == AvailableModelSourceType.HuggingFace:
            if self.model_source_path is None:
                self.model_source_path = "black-forest-labs/FLUX.1-dev"
            # For HuggingFace, no further validation needed - accept the path as-is
        elif self.model_source_type == AvailableModelSourceType.Local:
            if self.model_source_path is None:
                FluxionLogger("Model source path is required for Local model source type", "error")
                return
            if os.path.exists(self.model_source_path) and "model_index.json" in os.listdir(self.model_source_path):
                self.model_source_path = os.path.abspath(self.model_source_path)
            elif os.path.exists(self.model_source_path) and "model_index.json" not in os.listdir(self.model_source_path):
                FluxionLogger(f"Model index.json not found in the model source path {self.model_source_path}", "error")
            else:
                FluxionLogger(f"Model source path {self.model_source_path} does not exist", "error")
        elif self.model_source_type == AvailableModelSourceType.ZIP_URL:
            assert self.model_source_path is not None, "Model source path is required for ZIP_URL"
            
            
    @classmethod
    def from_dict(cls, config: dict):
        # Helper function to safely get values with defaults
        def safe_get(key, default_value, converter=None):
            value = config.get(key)
            if value is None or value == "":
                return default_value
            return converter(value) if converter else value
        
        return cls(
            model_source_type=safe_get(
                "model_source_type", 
                AvailableModelSourceType.HuggingFace,
                AvailableModelSourceType.from_str
            ),
            model_source_path=safe_get("model_source_path", "black-forest-labs/FLUX.1-dev"),
            model_format=safe_get(
                "model_format", 
                AvailableModelFormat.Diffusers,
                AvailableModelFormat.from_str
            ),
            pipeline_type=safe_get(
                "pipeline_type", 
                [AvailablePipelineType.Txt2Img],
                AvailablePipelineType.from_list
            ),
            pipeline_config=PipelineConfig.from_dict(config.get("pipeline_config", {})),
            device=safe_get(
                "device", 
                AvailableDevice.GPU,
                AvailableDevice.from_str
            ),
            dtype=safe_get(
                "dtype", 
                AvailableDtype.BFloat16,
                AvailableDtype.from_str
            ),
            attention_backend=safe_get(
                "attention_backend", 
                AvailableAttentionBackends.FAST_ATTENTION,
                AvailableAttentionBackends.from_str
            ),
            caching=safe_get(
                "use_caching", 
                AvailableCaching.FBCACHE,
                AvailableCaching.from_str
            ),
            compilation=safe_get(
                "compile", 
                AvailableCompilation.NONE,
                AvailableCompilation.from_str
            ),
            quantization=safe_get(
                "quantization", 
                AvailableQuantization.FP8,
                AvailableQuantization.from_str
            ),
        )
        
        
        
def generate_default_server_configs():
    config = ServerConfig()
    return to_json_dict(config)
        
def to_json_dict(obj):
    """Recursively converts objects to JSON-compatible dictionaries."""
    if isinstance(obj, Enum):
        return obj.value  # Convert Enums to their string values
    if hasattr(obj, "__dict__"):
        return {
            key: to_json_dict(value) for key, value in obj.__dict__.items()
        }  # Convert class instances
    if isinstance(obj, dict):
        return {
            key: to_json_dict(value) for key, value in obj.items()
        }  # Convert nested dicts
    if isinstance(obj, list):
        return [to_json_dict(item) for item in obj]  # Convert lists
    return obj

        