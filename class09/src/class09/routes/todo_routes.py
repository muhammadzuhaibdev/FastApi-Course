from fastapi import APIRouter
from pydantic import BaseModel
from bson.objectid import ObjectId
from class09.config.db_connection import db

todoRouter = APIRouter()

todo_collection = db['todos']

class Todo(BaseModel):
    title: str
    location: str
    description: str
    status: bool

@todoRouter.post('/create')
def create_todo(todoData: Todo):
    try:
        convert_dict = todoData.dict()
        
        result = todo_collection.insert_one(convert_dict)
        new_todo = todo_collection.find_one({"_id":  result.inserted_id})
        new_todo['_id'] = str(new_todo["_id"])
        
        return{
            "status": "success",
            "data": new_todo,
            "message": "Todo created Successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        
        
@todoRouter.get('/fetch')
def fetch_todos():
    try:
        result = list(todo_collection.find())
        print("result", result)
        
        for todo in result:
            todo["_id"] = str(todo["_id"])
        
        return {
            "status": "success",
            "data": result,
            "message": "Todos Fetched Successfully!"
        }
    except Exception as e:
        return  {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        
@todoRouter.get("/search")
def getSingleTodo(todoId):
    try:
        result = todo_collection.find_one({"_id": ObjectId(todoId)})
        result["_id"] = str(result["_id"])
        
        return{
            "status": "success",
            "data": result,
            "message": "Todo get successfully!"
        }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e)
        }
        
        
@todoRouter.put('/update/{id}')
def fetch_todos(id, todoData: Todo):
    try:
        updated_data = todoData.dict()
        result = todo_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        
        if result.matched_count == 0:
            return {"message": "Todo not Found"}
        
        return  {
            "status": "success",
            "data": [],
            "message": "Todos Updated Successfully!"
        }
    except Exception as e:
        return  {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        
@todoRouter.delete('/delete/{id}')
def fetch_todos(id):
    try:
        result = todo_collection.delete_one({"_id": ObjectId(id)})
        print(result)
        
        if result.deleted_count == 0:
            return ({"message": "Todo Not Found"})
        
        
        return  {
            "status": "success",
            "message": "Todos Deleted Successfully!"
        }
    except Exception as e:
        return  {
            "status": "error",
            "data": [],
            "message": str(e)
        }