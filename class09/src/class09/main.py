import uvicorn
from fastapi import FastAPI
from class09.routes.todo_routes import todoRouter

app = FastAPI()

app.include_router(todoRouter, prefix='/todo', tags=['todos'])


@app.get('/')
def server_running():
    return {"message": "Server is running"}


def start():
    uvicorn.run('class09.main:app',host='127.0.0.1', port=8080, reload=True)