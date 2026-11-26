from src.pdf_processor import extract_text
from src.text_cleaner import clean_text
from src.text_chunker import chunk_text
from src.metadata_extractor import extract_metadata
from src.structured_output import create_structured_output

def process_pdf(pdf_path):
    metadata = extract_metadata(pdf_path)

    raw_text = extract_text(pdf_path)

    if raw_text is None:
        chunks = []

    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)

    return create_structured_output(
        pdf_file = pdf_path.split("/")[-1],
        metadata = metadata,
        chunks = chunks
    )
