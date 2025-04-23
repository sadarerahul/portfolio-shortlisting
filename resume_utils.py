import os
import docx2txt
import pdfplumber

def extract_text_from_resume(file):
    ext = os.path.splitext(file.name)[1]
    text = ""

    if ext == ".pdf":
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    elif ext == ".docx":
        text = docx2txt.process(file)
    elif ext == ".txt":
        text = file.read().decode("utf-8", errors="ignore")
    else:
        text = "Unsupported file format."
    
    return text
