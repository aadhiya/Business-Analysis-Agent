# backend/file_processor.py

import pdfplumber
import io

def extract_text_from_pdf(file_bytes):
    text = ""
    file_stream = io.BytesIO(file_bytes)  # FIX: wrap bytes as file-like stream
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()
