from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException
import asyncio
import time
app= FastAPI()

class user(BaseModel):
    name: str
    age: int

class user1(BaseModel):
    name: Optional[str] =None
    age: Optional[int] =None

@app.get("/hello")
def hello(name:str):
    return name

@app.post("/hello")
def hello(users: user):
    return users.name

@app.put("/hello")
def hello(users: user):
    return users

@app.patch("/hello")
def hello(users: user1):
    return users


@app.get("/hello/{name}")
def hello(name:str):
    return name

@app.post("/user")
def check(user_id:str):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            details= "User not found"
        )
    return {"user": user_id}

@app.get("/sync")
def sync_call():
    time.sleep(3)
    return {"response": "done"}

@app.get("/async")
async def async_call():
    await asyncio.sleep(3)
    return {"response": "done"}