from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import random

my_data = []

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.post("/", response_class=HTMLResponse)
async def get_data(request:Request, task_name:str = Form(), task_description:str = Form(), task_priority:str = Form()):
    data = {
        "uid_number": get_uid_number(),
        "task_name": task_name,
        "task_description": task_description,
        "task_priority": task_priority,
        "task_date": datetime.today().strftime("%b %d, %Y ")
    }

    my_data.append(data)
    context = {"request": request, "my_data": my_data}


    return templates.TemplateResponse("index.html", context)

@app.get("/{uid_number}", response_class=HTMLResponse)
async def delete_data(request:Request, uid_number):
    for data in my_data:
        if data["uid_number"]==uid_number:
            my_data.remove(data)
    
    context = {"request": request, "my_data": my_data}

    return templates.TemplateResponse("index.html", context)

def get_uid_number():
    return f"{random.randint(000000,999999):06}"



