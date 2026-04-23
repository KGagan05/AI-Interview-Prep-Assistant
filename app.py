from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from generator import generate_questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, role: str = Form(...)):

    output = generate_questions(role)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "output": output,
        "role": role
    })