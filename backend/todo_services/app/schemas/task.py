from pydantic import BaseModel

class TokenData(BaseModel):
    token: str

class Task(BaseModel):
    id: str
    title: str
    description: str