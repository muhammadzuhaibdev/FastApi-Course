import os
import shutil
from fastapi import APIRouter, UploadFile, File

userRouter = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "upload")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@userRouter.post("/uploadFile")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "data": f"/static/{file.filename}",
        "message": "File Uploaded Successfully!"
    }
