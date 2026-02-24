from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import json


class Content(BaseModel):
    title: str
    body: str


app = FastAPI()


@app.get("/")
async def test_function():
    return "Hello, World!"



@app.post("/message")
async def receive_message(message_content: Dict[str,str]):
    try:
        #send message using google keep api
        return
    except:
        return {"message":"failiure"}




# update project list
@app.post("/projects")
async def receive_projects(project_content: Dict[str,str]):
    try:
        try:
            with open(r"data.json", "rw") as project_data_file:
                project_data_file_content=json.loads(project_data_file.read())
                project_data_file_content[]=project_content[]
                project_data_file.write(json.dumps(project_data_file_content))

        except:
            return
        return
    except:
        return {"message":"failiure"}
    

# remove a project
@app.delete("/projects")
async def remove_project(project_content: Dict[str,str]):
    try:
        try:
            with open(r"data.json", "rw") as project_data_file:
                project_data_file_content=json.loads(project_data_file.read())
                project_data_file_content[]
                project_data_file.write(json.dumps(project_data_file_content))

        except:
            return
        return
    except:
        return {"message":"failiure"}
    

# modify a project
@app.put("/projects")
async def modify_projects(project_content: Dict[str,str]):
    try:
        try:
            with open(r"data.json", "rw") as project_data_file:
                project_data_file_content=json.loads(project_data_file.read())
                project_data_file_content[]=project_content[]
                project_data_file.write(json.dumps(project_data_file_content))

        except:
            return
        return
    except:
        return {"message":"failiure"}
    




