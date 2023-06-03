from fastapi import APIRouter

from app.utils import predict_with_model

router = APIRouter()


@router.get("/{target}")
async def knn_prediction(target: str):
    classifier = "knn" 
    prediction = predict_with_model(classifier, target)
    return {"prediction": prediction}
