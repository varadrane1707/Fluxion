"""
Source Code : https://github.com/chengzeyi/ParaAttention/blob/main/src/para_attn/first_block_cache/utils.py
"""


import contextlib
import dataclasses
from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional, Union

from pydantic import BaseModel

from .para_attn_primitives import get_group, get_rank, get_world_size


class FirstBlockCache(BaseModel):
    pass