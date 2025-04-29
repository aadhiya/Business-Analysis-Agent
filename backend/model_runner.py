# backend/model_runner.py

import requests

def generate_business_report(file_text):
    prompt = f"Analyze the following business document and summarize key insights clearly and professionally:\n\n{file_text}\n\nSummary:"
    
    print("\n=== PROMPT START ===\n", prompt[:500], "\n=== PROMPT END ===")
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",   # You can change this later to phi, llama2, etc.
            "prompt": prompt,
            "stream": False          # For simple first test. (We can enable live streaming next.)
        }
    )
    
    output = response.json()
    result = output["response"]
    
    print("\n=== RESPONSE GENERATED ===\n", result[:500], "\n=== RESPONSE END ===")
    
    return result.strip()
