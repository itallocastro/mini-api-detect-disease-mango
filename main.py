from fastapi import FastAPI, UploadFile, File
from typing import Annotated
from src.model.service import predict

app = FastAPI()

BASE_URL = '/api/predict'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post(BASE_URL)
async def predict_image(file: Annotated[UploadFile, File(...)]):
    return await predict(file)
