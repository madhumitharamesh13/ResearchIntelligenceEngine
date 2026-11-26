def create_structured_output(pdf_file,metadata,chunks):
    structured_data = {
        "pdf_file:" : pdf_file,
        "metadata" : metadata,
        "chunks" : [
            {
                "chunk_id" : i+1,

                "text" : chunk

            }

            for i,chunk in enumerate(chunks)
        ]
    }

    return structured_data