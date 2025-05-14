# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
db = {}  # Simulated in-memory "database"

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get('/table')
async def check(name: str):
    return {"message": f"The table name is {name}"}

class User(BaseModel):
    username: str
    email: str

@app.post("/users/")
def create_user(user: User):
    if user.username in db:
        raise HTTPException(status_code=400, detail="User already exists")
    db[user.username] = user.dict()
    return {"message": "User created", "user": user}

@app.put("/users/{username}")
def update_user(username: str, user: User):
    if username not in db:
        raise HTTPException(status_code=404, detail="User not found")
    db[username] = user.dict()
    return {"message": "User updated", "user": user}