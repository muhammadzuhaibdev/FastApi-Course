from fastapi import FastAPI,Request
import uvicorn
from practice_project.routes.user_routes import userRouter
import time

app = FastAPI()

# @app.middleware('http')
# async def simple_middleware(request:Request, call_next):
#     print("Request enter to Middlware")
#     print(request.method)
#     print(request.headers)
#     print(request.url.path)
    
#     response = await call_next(request)
#     response.headers['MY-App'] = "Hello World"
    
#     print("Request out from Middlware")
#     return response


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = time.time()
    print(start_time)

    response = await call_next(request) 

    process_time = time.time() - start_time
    print(process_time)
    print(f"Status Code: {response.status_code}")
    response.headers["X-Process-Time"] = str(process_time)

    return response


app.include_router(userRouter, prefix='/user', tags=["user Apis"])


@app.get('/')
def test():
    return {"message":"Server is Running"}


def start():
    uvicorn.run('practice_project.main:app',host='127.0.0.1', port=8080,reload=True)