# this file is for the external routes that are used by the client to interact with the server  

from fastapi import APIRouter
from ..utils.context_managers import ModelManager

router = APIRouter()

@router.get("/v1/health")
def health():
    return {"message": "Sever is running"}

@router.get("/v1/model")
def models():
    return {"model_dict":ModelManager.get_model_dict()}

# @router.get("/v1/models/{model_name}")
# def model(model_name: str):
#     return {"message": f"Model {model_name} is running"}

# @router.post("/v1/predict")
    