import pymupdf 

def extract_text(pdf_path):
    all_text = []

    try:
         doc = pymupdf.open(pdf_path)
         
    except(FileNotFoundError,pymupdf.FileDataError) as e: 
        print(f"Error opening file: {e}")
        return ""

    try:
        for page in doc:
                text = page.get_text()
                all_text.append(text)

    finally:
         doc.close()

    return "\n".join(all_text)