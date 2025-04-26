"""Example of basic inference using Fluxion."""

import torch
from fluxion import FluxionPipeline
from fluxion.utils import Timer, setup_logging

def main():
    """Run a simple inference example."""
    # Set up logging
    setup_logging()
    
    # Initialize pipeline
    pipeline = FluxionPipeline.from_pretrained("example_model")
    
    # Prepare input
    prompt = "A beautiful sunset over the ocean"
    
    # Run inference with timing
    with Timer("Inference"):
        output = pipeline.generate(
            prompt=prompt,
            num_inference_steps=20,
            guidance_scale=7.5
        )
    
    # Save output
    output.save("output.png")

if __name__ == "__main__":
    main() 