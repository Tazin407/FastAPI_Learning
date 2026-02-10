from main import app
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str  # We receive this

class UserOut(BaseModel):
    username: str  # We only want to send THIS back

@app.post("/user/", response_model=UserOut)
def create_user(user: UserIn):
    # In a real app, you'd save to a DB here
    print("hello")
    return user