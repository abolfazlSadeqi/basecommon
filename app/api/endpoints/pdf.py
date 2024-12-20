import fitz
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.pdf_service import pdf_to_bytes, bytes_to_pdf
import os

router = APIRouter()

from fastapi.responses import FileResponse
from pydantic import BaseModel
import base64
import os

router = APIRouter()


class PDFBytesModel(BaseModel):
    pdf_bytes: str
    file_name: str


def bytes_to_pdf(pdf_bytes: bytes, output_path: str):
    print('ddd')
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)
        f.close()


@router.post("/pdf/from_bytes/")
async def convert_bytes_to_pdf(pdf_model: PDFBytesModel):
    output_path = f"file.pdf"
    try:
        pdf_bytes = base64.b64decode(pdf_model.pdf_bytes)
        bytes_to_pdf(pdf_bytes, output_path)
        return FileResponse(output_path, filename=pdf_model.file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except PermissionError:
                pass  # Handle the case where the file is still in use
