from fluxion.models import FluxTransformer
from fluxion.utils.config import OptimisationConfig


class FluxTxt2ImgPipeline:
    def __init__(self, model: FluxTransformer, optims: OptimisationConfig):
        self.model = model
        self.optims = optims
        
        
        