from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uploadFile import upload_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

app.include_router(upload_router)

@app.get("/")
async def root():
    return FileResponse("static/html/index.html", media_type="text/html")

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/jinja2")
async def jinja2(request: Request):
    data = {"title": "FastAPI with Jinja2", "message": "Jinja2 Message"}
    return templates.TemplateResponse("index.html", {"request": request, **data})