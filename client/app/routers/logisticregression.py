from fastapi import APIRouter

from app.utils import predict_with_model

router = APIRouter()


@router.get("/{target}")
async def logisticregression_prediction(target: str):
    classifier = "logisticregression"
    prediction = predict_with_model(classifier, target)
    return {"prediction": prediction}
