from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil
from count_people import count_people

uploade_router = APIRouter()
uploade_router.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

@uploade_router.get("/upload")
async def upload_page():
    return FileResponse("static/html/upload_image.html", media_type="text/html")

@uploade_router.post("/upload")
async def upload_image(file: UploadFile, request: Request):
    # 이미지 파일 확장자 확인
    file_extension = Path(file.filename).suffix # 파일 확장자를 문자열로 추출
    if file_extension not in ['.jpg', '.jpeg', '.png']:
        raise HTTPException(status_code=400, detail="Invalid image file type")

    # 이미지 파일 저장
    image_file_path = f'static/images/{file.filename}'
    with open(image_file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(image_file_path)
    n = count_people(image_file_path)
    print(n)

    result_path = f'static/results/result_of_{file.filename}'
    data = {"title": "FastAPI with Jinja2", "message": f"{n} people!"}
    return templates.TemplateResponse("image_result.html", {"request": request, "path": result_path, **data})