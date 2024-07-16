from fastapi import FastAPI
from .routers import tasks
# from .dependencies import get_dynamodb

app = FastAPI()

app.include_router(tasks.router)

# @app.on_event("startup")
# def startup_event():
#     get_dynamodb()


# from fastapi import FastAPI, Depends, HTTPException, Security
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel
# from typing import List
# # import boto3
# import requests

# app = FastAPI()

# # dynamodb = boto3.resource('dynamodb')
# # table = dynamodb.Table('todo_tasks')

# # Endpoint del servizio di autenticazione
# AUTH_SERVICE_URL = "http://192.168.1.174:8001/users/me"

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://192.168.1.174:8001/token")

# class Task(BaseModel):
#     id: str
#     title: str
#     description: str

# class TokenData(BaseModel):
#     token: str

# def verify_token(token: str = Security(oauth2_scheme)):
#     response = requests.get(AUTH_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Could not validate credentials")
#     return response.json()

# @app.get("/")
# async def root():
#     return {"message", "breath!!!"}

# @app.post("/verify-token")
# async def verify_token_route(token_data: TokenData):
#     token = token_data.token
#     response = requests.get(AUTH_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Could not validate credentials")
#     return response.json()

# # @app.post("/tasks/", response_model=Task)
# # async def create_task(task: Task, user: dict = Depends(verify_token)):
# #     table.put_item(Item=task.dict())
# #     return task

# # @app.get("/tasks/", response_model=List[Task])
# # async def read_tasks(user: dict = Depends(verify_token)):
# #     response = table.scan()
# #     return response.get('Items', [])

# # @app.get("/tasks/{task_id}", response_model=Task)
# # async def read_task(task_id: str, user: dict = Depends(verify_token)):
# #     response = table.get_item(Key={'id': task_id})
# #     if 'Item' not in response:
# #         raise HTTPException(status_code=404, detail="Task not found")
# #     return response['Item']

# # @app.put("/tasks/{task_id}", response_model=Task)
# # async def update_task(task_id: str, task: Task, user: dict = Depends(verify_token)):
# #     table.update_item(
# #         Key={'id': task_id},
# #         UpdateExpression="set title=:t, description=:d",
# #         ExpressionAttributeValues={
# #             ':t': task.title,
# #             ':d': task.description,
# #         },
# #         ReturnValues="UPDATED_NEW"
# #     )
# #     return task

# # @app.delete("/tasks/{task_id}", response_model=Task)
# # async def delete_task(task_id: str, user: dict = Depends(verify_token)):
# #     response = table.delete_item(Key={'id': task_id})
# #     return {"message": "Task deleted"}
