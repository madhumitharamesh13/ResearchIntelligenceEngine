import pymupdf

def extract_metadata(pdf_path):
    doc = pymupdf.open(pdf_path)

    metadata = doc.metadata

    structured_metadata = {
        "title" : metadata.get("title"),
        "author" : metadata.get("author"),
        "subject" : metadata.get("subject"),
        "keywords" : metadata.get("keywords"),
        "page_count" : len(doc)
    } 

    doc.close()
    
    return structured_metadata