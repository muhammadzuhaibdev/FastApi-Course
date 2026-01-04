from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/getCurrentUser')
def getCurrentUser():
    print('Get Current User Api Called')
    return 'Get Current User Api Called'

@app.post('/createUser')
def createUser():
    print('Create User Api Called')
    return 'Create User Api Called'

@app.put('/updateUser')
def updateUser():
    print('Update User Api Called')
    return 'Update User Api Called'

@app.delete('/deleteUser')
def deleteUser():
    print('Delete User Api Called')
    return 'Delete User Api Called'

def start():
    uvicorn.run('todos.main:app',host='127.0.0.1', port=8080,reload=True)