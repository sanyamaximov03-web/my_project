from fastapi import FastAPI, Body, HTTPException
from typing import Any
from api_handler import FastAPIHandler

app = FastAPI()
handler = FastAPIHandler()

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
    except (ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=422,
            detail=str(error)
        ) from error



    return {
        "item_id": item_id,
        "price": prediction
    }


