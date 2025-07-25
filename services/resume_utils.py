import os
import docx2txt
import pdfplumber

def extract_text_from_resume(file):
    """
    Extract text from PDF, DOCX, or TXT resumes.
    file: FastAPI UploadFile or file-like object
    """
    ext = os.path.splitext(file.filename)[1]
    text = ""

    if ext == ".pdf":
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif ext == ".docx":
        text = docx2txt.process(file.file)
    elif ext == ".txt":
        text = file.file.read().decode("utf-8", errors="ignore")
    else:
        text = "Unsupported file format."

    return text.strip()
