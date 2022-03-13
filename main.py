from fastapi import FastAPI ,Request, Response
import uvicorn
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

Department  = {"Mechanical":"Cloud","IT":"Informatica","EC":"Pipeline","Chemical":"Road"}

Employ = {
    1:{"Name":"Abhishek","Surname":"Vij" },
    2:{"Name":"Rohit","Surname":"Sharma" },
    3:{"Name":"Sachin","Surname":"Tendulkar"}
}


@app.api_route("/employee-details/{id}", methods=["GET"])
def get_employee_details (id:int):
        return Employ[id]
