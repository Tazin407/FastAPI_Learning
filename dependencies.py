from typing import Annotated
from fastapi import Depends, Header, HTTPException

def common_parameters(q: str = None, limit: int = 100):
    return {"q": q, "limit": limit}

def verify_token(x_token: Annotated[str, Header()] = None):
    if x_token != "super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token


