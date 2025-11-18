from fastapi import FastAPI, UploadFile
import shutil
import sys, os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.predict import predict_sound

app = FastAPI()

@app.post("/predict")
async def pred(file: UploadFile):
    path = "temp.wav"
    with open(path, "wb") as b:
        shutil.copyfileobj(file.file, b)
    return {"sound": predict_sound(path)}
