import base64
from http.client import HTTPException
from io import BytesIO
from PIL import Image
import requests
from loguru import logger
from fastapi import HTTPException



def download_image(image_url: str):
    if image_url.startswith('http'):
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            return HTTPException(status_code=400, detail=f"Error downloading image from {image_url}: {str(e)}")
    else:
        try:
            if image_url.startswith('data:image'):
                image_url = image_url.split(',')[1]
            image = Image.open(BytesIO(base64.b64decode(image_url)))
        except Exception as e:
            return HTTPException(status_code=400, detail=f"Error Decoding Base64 image from {image_url}: {str(e)}")
    return image