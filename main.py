from fastapi import FastAPI, Depends
from typing import Annotated
from dependencies import common_parameters, verify_token
 

app = FastAPI(dependencies=[Depends(verify_token)])

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/greet")
def greet_user(name : str = "Guest"):
    return {"message": f"Hello, {name}!"}

#phase 6
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price * 1.2}

#phase 7
class UserIn(BaseModel):
    username: str
    password: str  # We receive this

class UserOut(BaseModel):
    username: str  # We only want to send THIS back

@app.post("/user/", response_model=UserOut)
def create_user(user: UserIn):
    # In a real app, you'd save to a DB here
    return user

@app.get("/users/{user_id}/items/")
def read_user_items(user_id: int, q: str = None, limit: int = 10):
    return {"user_id": user_id, "query": q, "limit": limit}

#phase 8
@app.get("/items/")
async def read_items(params: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Items list", "params": params}

#phase 9
@app.get("/protected-data/")
def secret_data(token: Annotated[str, Depends(verify_token)]):
    return {"data": "The Krabby Patty formula is..."}


# Phase 10: Path Operations & HTTP Status Codes
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    return {"name": name, "note": "Created!"}

# Phase 11: apply everything in a professional endpoint
class ProfileUpdate(BaseModel):
    bio: str
    age: int
    
@app.put("/users/{user_id}/update_profile/", status_code=202)
def update_profile(user_id: int, profile: ProfileUpdate, notify : bool = False):
    return {"user_id": user_id, "status": "updated"}