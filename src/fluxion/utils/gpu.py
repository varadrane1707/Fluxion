from pynvml import GPUStats
from loguru import logger
import torch

def check_gpu_availability():
    logger.info("Checking GPU availability")
    gpu_stats = GPUStats()
    gpu_stats.get_gpu_info()
    logger.info(f"GPU count: {gpu_stats.gpu_count}")
    logger.info(f"GPU names: {gpu_stats.gpu_names}")
    logger.info(f"GPU memory: {gpu_stats.gpu_memory}")
    logger.info(f"GPU temperature: {gpu_stats.gpu_temperature}")
    logger.info(f"GPU power: {gpu_stats.gpu_power}")
    logger.info(f"GPU fan speed: {gpu_stats.gpu_fan_speed}")
    logger.info(f"GPU utilization: {gpu_stats.gpu_utilization}")
    return gpu_stats.gpu_count > 0

def check_cuda_availability():
    return torch.cuda.is_available()

