import numpy
import tensorflow
import pandas
from fastapi import FastAPI
import mediapipe


app = FastAPI(title="Accountable Workout API")

@app.get("/")
def health_check():
    return {"status": 'ok'}

