import uvicorn
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI
import json

app = FastAPI()


class insuranceCost(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str


@app.get("/")
def Index():
    return {
        "Welcome": "To Insurance Prediction"
    }


@app.post("predictcost")
def predict(data: insuranceCost):
    data = [[data.age, data.sex, data.bmi, data.children,  # type: ignore
             data.smoker, data.region]]
    return data



if __name__ == "__main__":
    uvicorn.run(app)