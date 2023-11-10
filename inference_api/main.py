import os.path
from typing import Union
import aiofiles
from fastapi import FastAPI, UploadFile, File
from infrustructure.detector import *


app = FastAPI()
yolo_detector = YoloV5Detector("infrustructure/best.pt")
UPLOAD_PATH = "uploads"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/file/")
async def upload_file(file: UploadFile):
    out_path = os.path.join(UPLOAD_PATH, file.filename)
    async with aiofiles.open(out_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    res = yolo_detector.detect_contours(out_path)
    preds = []
    for i in res:
        preds.append(i.dict())
    print(preds)
    return {"filename": file.filename, "results": preds}
