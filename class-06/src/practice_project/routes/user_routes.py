from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

userRouter = APIRouter()

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int
    rollNo: Optional[str] = 'ES7-345678' 

@userRouter.get('/getAll')
def getAllUser():
    try:
        userData= [
            {"id":1, "name":"zuhaib", "email":"zuhaib@gmail.com"},
            {"id":2, "name":"Hamza",  "email":"hamza@gmail.com"},
            {"id":3, "name":"Abdullah",  "email":"abdullah@gmail.com"},
        ]
        return {
            "status": "success",
            "data": userData,
            "message": "Users Data Fetched Successfully!"
        }
    except Exception as e:
        return {
            "status":"error",
            "data":[],
            "message":str(e)
        }
        
@userRouter.post('/createUser')
def createUser(userData: UserSchema):
    try:
        return {
            "status":"success",
            "data": userData,
            "message": "User Created Successfully!"
        }
    except Exception as e:
        print("Error creating user", e)
        return{
            "status":"error",
            "data":[],
            "message": str(e)
        }
