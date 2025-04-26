from Pydantic import BaseModel

class QuantizationConfig(BaseModel):
    backend: str
    dtype: str
    quant_type: str
    extra_parameters: dict
    
