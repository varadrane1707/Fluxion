from Pydantic import BaseModel
from enum import Enum
from typing import Literal

from caching import __allowed_caching_types__

class ExtraParameters(BaseModel):
    threshold: float

class CachingConfig(BaseModel):
    caching_type: Literal[__allowed_caching_types__]
    caching_file_path: str
    enabled: bool
    extra_parameters: ExtraParameters
    