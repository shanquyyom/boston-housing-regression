from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load the saved model
model = joblib.load("model.pkl")

# Input schema
class HouseData(BaseModel):
    crim: float
    zn: float
    indus: float
    chas: int
    nox: float
    rm: float
    age: float
    dis: float
    rad: int
    tax: int
    ptratio: float
    b: float
    lstat: float

@app.post("/predict")
def predict_price(data: HouseData):
    input_data = np.array([[ 
        data.crim, data.zn, data.indus, data.chas, data.nox,
        data.rm, data.age, data.dis, data.rad, data.tax,
        data.ptratio, data.b, data.lstat
    ]])

    prediction = model.predict(input_data)
    return {"Predicted Price (in $1000s)": round(prediction[0], 2)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
