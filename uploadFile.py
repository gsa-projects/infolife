from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

upload_router = APIRouter()

@upload_router.get("/upload")
async def upload_page():
    return FileResponse("static/html/upload_image.html", media_type="text/html")

@upload_router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # 이미지 파일 확장자 확인
    file_extension = Path(file.filename).suffix     # 파일 확장자를 문자열로 추출
    if file_extension not in ['.jpg', '.jpeg', '.png']:
        raise HTTPException(status_code=400, detail="Invalid image file type")

    # 이미지 파일 저장
    image_file_path = f'static/images/{file.filename}'      # 파일 저장 경로
    with open(image_file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)