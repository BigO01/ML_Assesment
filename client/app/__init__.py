from fastapi import FastAPI

from app.routers import knn, randomforest, svm, logisticregression

app = FastAPI()

app.include_router(knn.router, prefix="/knn", tags=["KNN"])
app.include_router(randomforest.router, prefix="/randomforest", tags=["Random Forest"])
app.include_router(svm.router, prefix="/svm", tags=["SVM"])
app.include_router(logisticregression.router, prefix="/logisticregression", tags=["Logistic Regression"])
