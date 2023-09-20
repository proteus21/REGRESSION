from fastapi import FastAPI,Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class BMIRequest(BaseModel):
    height: float
    weight: float

@app.post("/calculate_bmi")
async def calculate_bmi(request: Request, height: float = Form(...), weight: float = Form(...)):


    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return {"BMI": bmi, "Category": category}

@app.get("/bmi_calculator", response_class=HTMLResponse)
async def get_bmi_calculator(request: Request):
    return templates.TemplateResponse("bmi_calculator.html", {"request": request})