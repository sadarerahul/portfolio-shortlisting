from fastapi import APIRouter, Form
from services.email_generator import send_email_with_resume, generate_email

router = APIRouter()

@router.post("/send-mail")
async def send_mail(
    candidate_email: str = Form(...),
    resume_file: str = Form(...),
    hr_email: str = Form(...),
    hr_password: str = Form(...),
    company_name: str = Form("Your Company")  # You can pass company_name if available
):
    """Send LLM-generated email with candidate's resume attached."""

    # ✅ 1) Generate a professional email using LLM
    portfolios_text = f"Dear {candidate_email},\nYou are shortlisted for {company_name}."
    email_body = generate_email(portfolios_text, company_name)

    # ✅ 2) Send the mail with generated body
    result = send_email_with_resume(
        recipients=[candidate_email],
        subject=f"Shortlisted for {company_name}",
        body=email_body,
        attachments=[resume_file],
        hr_email=hr_email,
        hr_password=hr_password
    )
    return result
