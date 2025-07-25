from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from services.shortlisting import shortlist_candidates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/main", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/shortlist", response_class=HTMLResponse)
async def shortlist(request: Request,
                    company_name: str = Form(...),
                    job_post: UploadFile = File(...),
                    resumes: list[UploadFile] = File(...),
                    top_k: int = Form(...)):
    # Save job post temporarily
    job_text = (await job_post.read()).decode("utf-8", errors="ignore")

    # Save resumes to uploads folder
    saved_files = []
    for file in resumes:
        file_path = os.path.join("uploads", file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        saved_files.append({"file": file, "path": file_path})

    results = shortlist_candidates(job_text, saved_files, top_k, company_name)

    return templates.TemplateResponse("results.html", {
    "request": request,
    "candidates": results["candidates"],
    "email": results["email"],
    "company_name": company_name  # ✅ Now accessible in results.html
})

