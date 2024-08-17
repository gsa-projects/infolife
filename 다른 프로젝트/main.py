from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from uploadFile import uploade_router
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

# 템플릿 객체 초기화
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@uploade_router.get("/testing")
async def upload_page():
    return FileResponse("resources/index.html", media_type="text/html")


app.include_router(uploade_router)