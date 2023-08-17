import json
import requests


SENSIBLE_API_KEY = "YOUR API KEY HERE"

def extract_content(d_type: str, d_name: str, env: str):
    url = "https://api.sensible.so/v0/extract/{}?environment={}".format(d_type, env)
    headers = {
        "Authorization": "Bearer {}".format(SENSIBLE_API_KEY),
        "content-type": "application/pdf"
    }
    
    with open(d_name, 'rb') as fp:
        pdf_file = fp.read()
        response = requests.post(url, headers=headers, data=pdf_file)

        print("Status code: {}".format(response.status_code))
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))

# 1. Extract content from a structured PDF file
document_type = "tax_forms"
document_name = "senior_1040_2019_sample.pdf"
environment = "production"

extract_content(document_type, document_name, environment)

# 2. Extract content from unstructured PDF files using the Query method

document_type = "research_paper"
document_name = "U-Net.pdf"
environment = "development"

extract_content(document_type, document_name, environment)

# 3. Extract content from unstructured PDF files using a Summarizer.
document_type = "reports"
document_name = "OPEC_MOMR_April_2023.pdf"

extract_content(document_type, document_name, environment)
