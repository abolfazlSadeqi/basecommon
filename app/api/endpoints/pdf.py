from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.pdf_service import pdf_to_bytes, bytes_to_pdf
import os

router = APIRouter()

@router.post("/pdf/to_bytes/")
async def convert_pdf_to_bytes(file: UploadFile = File(...)):
    try:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
            pdf_bytes = pdf_to_bytes(file_path)
            os.remove(file_path)
        return {"file_name": file.filename, "pdf_bytes": pdf_bytes}
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

@router.post("/pdf/from_bytes/")
async def convert_bytes_to_pdf(pdf_bytes: bytes, file_name: str):
    output_path = f"temp_{file_name}"
    try:
        bytes_to_pdf(pdf_bytes, output_path)
        return FileResponse(output_path, filename=file_name)
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except PermissionError:
              pass  # Handle the case where the file is still in use
