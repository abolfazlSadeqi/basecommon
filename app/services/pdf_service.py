import fitz  # PyMuPDF

def pdf_to_bytes(file_path: str) -> bytes:
    with open(file_path, "rb") as f:
     return f.read()

def bytes_to_pdf(data: bytes, output_path: str):
    with open(output_path, "wb") as f:
      f.write(data)