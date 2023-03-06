import os
import json
import requests


API_KEY = os.getenv('API_KEY')

def extract_content(d_type: str, d_name: str, env: str):
    """
    Extract content from a PDF file.
    """
    url = f"https://api.sensible.so/v0/extract/{d_type}?environment={env}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "content-type": "application/pdf"
    }

    with open(d_name, 'rb') as fp:
        pdf_file = fp.read()
        response = requests.post(url, headers=headers, data=pdf_file)
        
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))            
# 1. Extract content from a structured PDF file
document_type = "tax_forms"
document_name = "1040_2020_sample.pdf"
environment = "production"

extract_content(document_type, document_name, environment)

# 2. Extract content from unstructured PDF files using the Topic method

document_type = "legal_code"
document_name = "CC BY-NC-SA 4.0.pdf"
environment = "development"

extract_content(document_type, document_name, environment)

# 3. Extract content from unstructured PDF files using a Summarizer.
document_type = "reports"
document_name = "whs-22h.pdf"

extract_content(document_type, document_name, environment)