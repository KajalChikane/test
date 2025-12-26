# user= input("enter user name: ")
# print("Hi ", user)

# age= 19

# if age>= 18:
#     print("Adult")
# else: 
#     print("Not Adult")

# for x in range(5):
#     print(x)

# count=2
# while count<3:
#     print(count)
#     count += 1


# def greet(name, age):
#     return(f"Hello {name}. You are {age}")

# name= input("Enter name")
# age= input("Enter age")
# print(greet(name,age))

# number=10
# def even(number):
#     if(number %2 == 0):
#         return("Even")
#     else:
#         return("Odd")
    
# print(even(10))

# user = {
#     "name": "Kajal",
#     "role": "developer",
#     "skills": ["python", "ai"]
# }

# print(user["skills"])

# tools = ["calculate", "web", "simple"]
# tools.append("High")
# print(tools)
# for tool in tools:
#     print(tool)

# user = {
#     "name": "Kajal",
#     "role": "developer",
#     "active": True
# }

# user["Experience"] = "beginner"
# print(user)

# messages = [
#     {"role": "system", "content": "You are an assistant"},
#     {"role": "user", "content": "Hello"},
#     {"role": "assistant", "content": "Hi!"}
# ]

# print(messages[2]["content"])

# agent = {
#     "name": "SimpleAgent",
#     "tools": ["search", "calculator"],
#     "memory": []
# }

# agent["memory"].append("User asked about Python")
# agent["memory"].append("Explained basics")

# print(agent)

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/greet/{name}")
# def greet(name: str):
#     return {"greeting": f"Hello {name}"}

# @app.get("/agent/status")
# def status():
#     return {"agent": "SimpleAgent","status": "running"}

# from fastapi import FastAPI
# from llm import call_llm

# app = FastAPI()

# @app.post("/chat")
# def chat(prompt: str):
#     answer = call_llm(prompt)
#     return {"response": answer}


from fastapi import FastAPI
from agent_logic import agent_think
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    prompt: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for learning)
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)

@app.post("/agent/chat")
def agent_chat(request: ChatRequest):
    reply = agent_think(request.session_id, request.prompt)
    return {"reply": reply}
