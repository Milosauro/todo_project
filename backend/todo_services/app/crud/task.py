from ..schemas.task import Task
from ..dependencies import get_dynamodb

dynamodb = get_dynamodb()
table = dynamodb.Table('todo_tasks')

def create_task(task: Task) -> Task:
    table.put_item(Item=task.dict())
    return task

def get_tasks() -> List[Task]:
    response = table.scan()
    return response.get('Items', [])

def get_task(task_id: str) -> Task:
    response = table.get_item(Key={'id': task_id})
    return response.get('Item')

def update_task(task_id: str, task: Task) -> Task:
    table.update_item(
        Key={'id': task_id},
        UpdateExpression="set title=:t, description=:d",
        ExpressionAttributeValues={
            ':t': task.title,
            ':d': task.description,
        },
        ReturnValues="UPDATED_NEW"
    )
    return task

def delete_task(task_id: str):
    table.delete_item(Key={'id': task_id})