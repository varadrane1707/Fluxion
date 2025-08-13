import uuid
from fastapi import APIRouter
import uuid

router = APIRouter()

@router.get("/health")
def health():
    return {"message": "Server is running"}

@router.get("/version")
def version():
    return {"message": "1.0.0"}

@router.post("/v1/predict")
def predict(request_json: dict):
    correlation_id = request_json.get("correlation_id",uuid.uuid4())
    validation_queue.put(request_json)