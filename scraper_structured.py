import os
import json
import requests


API_KEY = os.getenv('API_KEY')
document_type = "tax_forms"#"senseml_basics"
document_name = "1040_2020_sample.pdf"

url = f"https://api.sensible.so/v0/extract/{document_type}?environment=production"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "content-type": "application/pdf"
}

with open(document_name, 'rb') as fp:
    file = fp.read()
    response = requests.post(url, headers=headers, data=file)
    
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))