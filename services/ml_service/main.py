from fastapi import FastAPI, Body, HTTPException
from typing import Any
from math import isfinite
from api_handler import FastAPIHandler
from prometheus_client import Histogram, Counter
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Car Price Prediction API", description="Сервис предсказания стоимости автомобилей", version="2.0")
handler = FastAPIHandler()

prediction_metric = Histogram("prediction_price", "Distribution of prediction car prices", buckets=(
    0, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 200, 500, 1000))


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/api/prediction")
def make_prediction(
    item_id: int,
    item_features: dict[str, Any] = Body(...)
):
    try:
        prediction = handler.predict(item_features)
        prediction = float(prediction)

        if not isfinite(prediction):
            raise ValueError("Model returned a non-finite prediction")
        
    except (ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=422,
            detail=str(error)
        ) from error

    prediction_metric.observe(prediction)



    return {
        "item_id": item_id,
        "price": prediction
    }

Instrumentator().instrument(app).expose(app, include_in_schema=False)
