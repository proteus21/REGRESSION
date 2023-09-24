import uvicorn
from fastapi import FastAPI, Form, Request
from Model import IrisModel, IrisSpecies
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
model = IrisModel()
templates = Jinja2Templates(directory="templates")

@app.post('/predict')
def predict_species(
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    prediction, probability = model.predict_species(
        sepal_length, sepal_width, petal_length, petal_width
    )
    return {
        'prediction': prediction,
        'probability': probability
    }

@app.get("/predict", response_class=HTMLResponse)
async def get_predict(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})
