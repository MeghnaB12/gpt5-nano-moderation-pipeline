import PyPDF2

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text content from a PDF file.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = []
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text.append(extracted)
            return "\n".join(text)
    except FileNotFoundError:
        raise ValueError("PDF file not found.")
    except Exception as e:
        raise RuntimeError(f"Failed to parse PDF: {e}")