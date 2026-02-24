from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any







app = FastAPI()

@app.get("/")
async def test_function():
    return "Hello, World!"



@app.post("/message")
async def receive_message(message_body: Dict[str,str]):
    try:
        #send message using google keep api
        return
    except:
        return {"message":"failiure"}





@app.put("/projects")
async def receive_projects(message_body: Dict[str,str]):
    try:
        #send message using google keep api
        return
    except:
        return {"message":"failiure"}
    




