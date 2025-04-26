"""Utilities module for Fluxion.

This module provides various utility functions including:
- Model utilities
- Memory management
- Performance profiling
- Logging and monitoring
"""

import torch
from typing import Optional, Union, Dict, Any
import logging
import time
from pathlib import Path

def setup_logging(
    log_level: Union[str, int] = logging.INFO,
    log_file: Optional[Union[str, Path]] = None
) -> None:
    """Set up logging configuration.
    
    Args:
        log_level: Logging level
        log_file: Optional path to log file
    """
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file
    )

class Timer:
    """Simple timer for performance measurements."""
    
    def __init__(self, name: str):
        """Initialize timer.
        
        Args:
            name: Timer name for identification
        """
        self.name = name
        self.start_time: Optional[float] = None
        
    def __enter__(self) -> 'Timer':
        self.start_time = time.perf_counter()
        return self
        
    def __exit__(self, *args: Any) -> None:
        if self.start_time is None:
            return
        elapsed = time.perf_counter() - self.start_time
        logging.info(f"{self.name} took {elapsed:.4f} seconds")
