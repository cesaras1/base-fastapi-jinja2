from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/")
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})
    