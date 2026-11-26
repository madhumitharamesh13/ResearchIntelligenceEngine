def chunk_text(text, chunk_size = 1000, overlap = 200):
    if not isinstance(text,str):
        raise TypeError("Input must be a string.")

    if chunk_size <= 0 :
        raise ValueError("Chunk size must be positive.")

    if overlap >= chunk_size or overlap < 0:
        raise ValueError("Overlap must be non-negative and smaller than chunk size.")
    
    if not text.strip():
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks