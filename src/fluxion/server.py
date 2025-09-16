import asyncio
from fluxion.engine import FluxionEngine
from loguru import logger
from fluxion.utils.config import ServerConfig


class FluxionServer():
    def __init__(self, config: ServerConfig ,loop: asyncio.AbstractEventLoop = None):
        
        self.loop = loop
        self.config = config
        self.engine = FluxionEngine(self.config)
        
    async def run(self):
        await self.engine.run()
        
    def run(self):
        self.engine.run()
        
        