import requests
from fastapi import HTTPException

from ..schemas.task import TokenData

AUTH_SERVICE_URL = "http://192.168.1.174:8001/users/me"

def verify_token(token: TokenData):
    print(token.token)
    response = requests.get(AUTH_SERVICE_URL, headers={"Authorization": f"Bearer {token.token}"})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Could not validate credentials")
    return response.json()