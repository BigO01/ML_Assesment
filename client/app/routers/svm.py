from fastapi import APIRouter

from app.utils import predict_with_model

router = APIRouter()


@router.get("/{target}")
async def svm_prediction(target: str):
    classifier = "svm"
    prediction = predict_with_model(classifier, target)
    return {"prediction": prediction}
