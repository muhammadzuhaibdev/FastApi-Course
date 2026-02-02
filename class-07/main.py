from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = './uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount('/static', StaticFiles(directory=UPLOAD_FOLDER), name='static')


@app.post('/upload')
def file_upload(file: UploadFile):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    file_url = f'/static/{file.filename}'
    
    return {"filename": file.filename, "fileurl": file_url }



@app.get('/')
def server_running():
    return {"message": "Server is running"}




# from fastapi import FastAPI, File, UploadFile
# from fastapi.staticfiles import StaticFiles
# import shutil
# import os

# app = FastAPI()

# UPLOAD_FOLDER = './uploads'

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app.mount('/static', StaticFiles(directory=UPLOAD_FOLDER), name='static')


# @app.post('/upload')
# def Upload_Files(file: UploadFile):
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
#     with open(file_path, 'wb') as buffer:
#         shutil.copyfileobj(file.file, buffer)
        
#     file_url = f"/static/{file.filename}"
    
#     return {"fileName": file.filename, "file_url": file_url}



# @app.get('/')
# def server_running():
#     return {"message", "Server is running"}