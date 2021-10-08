from fastapi import APIRouter, File, UploadFile
from typing import List

fileRouter = APIRouter()

@fileRouter.post("/uploadfile/")
async def upload_file(fileS: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in fileS]}