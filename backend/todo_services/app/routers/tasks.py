from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from ..schemas.task import Task, TokenData
# from ..crud.task import create_task, get_tasks, get_task, update_task, delete_task
from ..external_services.auth_service import verify_token

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    dependencies=[Depends(verify_token)],
)

@router.post("/verify_token")
async def verify_token_endpoint(token: TokenData):
    return verify_token

# @router.post("/", response_model=Task)
# async def create_task_endpoint(task: Task):
#     return create_task(task)

# @router.get("/", response_model=List[Task])
# async def read_tasks_endpoint():
#     return get_tasks()

# @router.get("/{task_id}", response_model=Task)
# async def read_task_endpoint(task_id: str):
#     task = get_task(task_id)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task

# @router.put("/{task_id}", response_model=Task)
# async def update_task_endpoint(task_id: str, task: Task):
#     return update_task(task_id, task)

# @router.delete("/{task_id}", response_model=Dict[str, str])
# async def delete_task_endpoint(task_id: str):
#     delete_task(task_id)
#     return {"message": "Task deleted"}