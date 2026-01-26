from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class User(BaseModel):
    id: Optional[str] = None
    name:str
    email:str
    age: int


@app.post('/createUser')
def getUser(userData:User):
    try:
        return{
            "status":"success",
            "data": userData,
            "message":"User data fetched Successfully!"
        }
    except Exception as e:
        print("Error creating User Data", e)
        return{
            "status": "error",
            "data": None,
            "message": str(e)
        }
    

@app.get('/getUser/{password}')
def getUser(password:int):
    try:
        if not password == 124421:
            return {
                "status": "error",
                "message": "Password is required"
            }
        
        return{ 
            "status":"success",
            "data": {
                "id":"76i8ycfghjfcf ghmngb",
                "name":"zuhaib",
                "email":"zuhaib@gmail.com",
                "phone": "3267127657"
            },
            "message":"User Data Fetched Successfully!" 
        }
    except Exception as e:
        print("Error Fetching User Data", e)
        return{
            "status": "error",
            "data": None,
            "message": str(e)
        }
        
