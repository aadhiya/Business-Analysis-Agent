# backend/app.py

from fastapi import FastAPI, UploadFile, File
from backend.file_processor import extract_text_from_pdf
from backend.agent_manager import handle_business_goal

app = FastAPI()

@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()
    text_content = extract_text_from_pdf(content)
    if not text_content:
        return {"error": "No text found in PDF. Please upload a readable document."}
    
    result = handle_business_goal(text_content)
    return {"result": result}  # ✅ Changed 'report' to 'result'
