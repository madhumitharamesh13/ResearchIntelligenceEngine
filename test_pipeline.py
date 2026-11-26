import json
from src.pipeline import process_pdf

pdf_path = "data/raw/short-research-paper-example.pdf"

result = process_pdf(pdf_path)

print(json.dumps(result,indent = 4))