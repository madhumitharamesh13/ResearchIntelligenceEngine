from src.pdf_processor import extract_text

pdf_path = "data/raw/short-research-paper-example.pdf"

extracted_text = extract_text(pdf_path)

print(extracted_text)