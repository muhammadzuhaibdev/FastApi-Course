import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.user_routes import userRouter

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "upload")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/static", StaticFiles(directory=UPLOAD_FOLDER), name="static")
app.include_router(userRouter, prefix="/user", tags=["user_routes"])

@app.get("/")
def server_running():
    return {"message": "Server is running"}
