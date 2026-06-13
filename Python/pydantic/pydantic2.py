from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    age : int

@app.post("/add_user/")
def create_user(user: User):   # typer hint incoming user should be of type user
    return f"User Created Successfully: User {user}"

