import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from langchain_core.prompts import ChatPromptTemplate
from services.llm_utils import llm


def generate_email(portfolios_text: str, company_name: str) -> str:
    """Generate a professional HR email using LLM."""
    email_prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are HR at {company_name}. Generate a formal email for shortlisted students."),
        ("human", "{input}")
    ])
    email_chain = email_prompt | llm
    result = email_chain.invoke({"input": portfolios_text})
    return result.content


def send_email_with_resume(
    recipients: list,
    subject: str,
    body: str,
    attachments: list = [],
    hr_email: str = None,
    hr_password: str = None
):
    """Send email with attachments via Gmail using HR's credentials."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(hr_email, hr_password)

        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = hr_email
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Attach files
            for file_path in attachments:
                if not os.path.exists(file_path):
                    continue
                filename = os.path.basename(file_path)
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                    )
                    msg.attach(part)

            server.sendmail(hr_email, recipient, msg.as_string())

        server.quit()
        return {"status": "success", "message": f"✅ Mail sent to {len(recipients)} recipients"}
    except Exception as e:
        return {"status": "error", "message": f"❌ Failed to send mail: {str(e)}"}
