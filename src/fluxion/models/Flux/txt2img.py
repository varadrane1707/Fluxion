from ...models.transformers import FluxTransformer2DModel
from ...models.autoencoders import AutoencoderKL
from fluxion.utils.config import OptimisationConfig
from typing import Optional,Union,List
import torch
from loguru import logger
from ..Loras import FluxLoraMixin


class FluxPipeline(
    FluxLoraMixin,
    OptimisationConfig,
):
    def __init__(self,
        scheduler: FlowMatchEulerDiscreteScheduler,
        vae: AutoencoderKL,
        text_encoder: CLIPTextModel,
        tokenizer: CLIPTokenizer,
        text_encoder_2: T5EncoderModel,
        tokenizer_2: T5TokenizerFast,
        transformer: FluxTransformer2DModel,
        image_encoder: CLIPVisionModelWithProjection = None,
        feature_extractor: CLIPImageProcessor = None,
        optims: OptimisationConfig = None,
    ):
        super().__init__()
        self.scheduler = scheduler
        self.vae = vae
        self.text_encoder = text_encoder
        self.tokenizer = tokenizer
        self.text_encoder_2 = text_encoder_2
        self.tokenizer_2 = tokenizer_2
        self.transformer = transformer
        
        self.vae_scale_factor = 2 ** (len(self.vae.config.block_out_channels) - 1) if getattr(self, "vae", None) else 8
        self.tokenizer_max_length = self.tokenizer.model_max_length if hasattr(self, "tokenizer") and self.tokenizer is not None else 77
        self.default_sample_size = 128
        self.image_encoder = image_encoder if image_encoder is not None else None
        self.feature_extractor = feature_extractor if feature_extractor is not None else None
        
        self.optims = optims
        self.device = self.optims.device
        self.dtype = self.optims.dtype
        
        
        def _get_t5_prompt_embeds(
        self,
        prompt: Union[str, List[str]] = None,
        num_images_per_prompt: int = 1,
        max_sequence_length: int = 512,
        device: Optional[torch.device] = None,
        dtype: Optional[torch.dtype] = None,
        ) -> torch.Tensor:
            device = self.device
            dtype = self.dtype

            prompt = [prompt] if isinstance(prompt, str) else prompt
            batch_size = len(prompt)

            if isinstance(self, TextualInversionLoaderMixin):
                prompt = self.maybe_convert_prompt(prompt, self.tokenizer_2)

            text_inputs = self.tokenizer_2(
                prompt,
                padding="max_length",
                max_length=max_sequence_length,
                truncation=True,
                return_length=False,
                return_overflowing_tokens=False,
                return_tensors="pt",
            )
            text_input_ids = text_inputs.input_ids
            untruncated_ids = self.tokenizer_2(prompt, padding="longest", return_tensors="pt").input_ids

            if untruncated_ids.shape[-1] >= text_input_ids.shape[-1] and not torch.equal(text_input_ids, untruncated_ids):
                removed_text = self.tokenizer_2.batch_decode(untruncated_ids[:, self.tokenizer_max_length - 1 : -1])
                logger.warning(
                    "The following part of your input was truncated because `max_sequence_length` is set to "
                    f" {max_sequence_length} tokens: {removed_text}"
                )

            prompt_embeds = self.text_encoder_2(text_input_ids.to(device), output_hidden_states=False)[0]

            dtype = self.text_encoder_2.dtype
            prompt_embeds = prompt_embeds.to(dtype=dtype, device=device)

            _, seq_len, _ = prompt_embeds.shape
            
            # duplicate text embeddings and attention mask for each generation per prompt, using mps friendly method
            prompt_embeds = prompt_embeds.repeat(1, num_images_per_prompt, 1)
            prompt_embeds = prompt_embeds.view(batch_size * num_images_per_prompt, seq_len, -1)
            return prompt_embeds
        
        
        
        
        
        
        
        
        
        
        
        