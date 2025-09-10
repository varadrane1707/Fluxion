import json
import os 
import sys
import argparse
from loguru import logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import FluxionServer
from utils.config import ServerConfig
from utils.gpu import check_gpu_availability, check_cuda_availability

from utils.constants import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config-path", type=str, required=True , help="Path to the config file for the Fluxion server")
    args = parser.parse_args()
    
    
    config = ServerConfig.from_dict(json.load(open(args.config_path)))
    if not check_gpu_availability() or not check_cuda_availability():
        logger.error("GPU or CUDA is not available. Please check your GPU configuration.")
        sys.exit(1)
    server = FluxionServer(config)
    
    with asyncio.run(server.run()):
    server.run()

    



