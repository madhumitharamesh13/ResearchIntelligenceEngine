from src.text_chunker import chunk_text

sample_text = "M"*2500

chunks = chunk_text(sample_text)
print("Total chunks: ", len(chunks))

for i,chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {len(chunk)} characters")

print(f"Chunk 1 starts at: {chunks[0][:10]}")
print(f"Chunk 2 starts at: {chunks[1][:10 ]}")