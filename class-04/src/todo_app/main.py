from fastapi import FastAPI
import uvicorn
app = FastAPI()

usersData = [
    {"id":1, "name":"zuhaib", "email":"zuhaib@gmail.com"},
    {"id":2, "name":"hamza", "email":"hamza@gmail.com"},
    {"id":3, "name":"abdullah", "email":"abdullah@gmail.com"}
]

@app.get("/getUsers")
def getUser():
    return usersData

@app.post('/createUser/{name}/{email}')
def createUser(name:str, email:str):
    usersData.append({"id": len(usersData) + 1, "name": name, "email":email})
    return usersData

@app.delete('/deleteUser')
def createUser(id):
    global usersData
    
    if not id: return {"message": "Id is required!"}    
    usersData = list(filter(lambda user: user["id"] != int(id), usersData))
    return usersData

def start():
    uvicorn.run('todo_app.main:app',host="127.0.0.1",port=8080,reload=True)