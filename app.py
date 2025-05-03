import streamlit as st 
import json
import os
from dotenv import load_dotenv
from llm_utils import extract_job_info
from email_generator import generate_email
from portfolios import init_resume_collection
from resume_utils import extract_text_from_resume
import uuid

load_dotenv()
st.set_page_config(page_title="Portfolio Shortlisting", layout="centered")

st.title("📂 Resume Shortlisting System")

# Upload job description
job_file = st.file_uploader("Upload Job Description", type=["txt", "pdf", "docx"])

# Upload multiple resumes
resumes = st.file_uploader("Upload Resumes Folder", type=["pdf", "docx", "txt"], accept_multiple_files=True)

# Number of best matches
top_k = st.number_input("Select number of best matches", min_value=1, max_value=10, value=3, step=1)

if job_file and resumes:
    job_text = job_file.read().decode("utf-8", errors="ignore")
    st.subheader("🔍 Extracting Job Info...")
    job_info_json = extract_job_info(job_text)

    try:
        job_info = json.loads(job_info_json.strip("`\n"))
        st.json(job_info)
    except Exception as e:
        st.error("❌ Failed to extract job info")
        st.stop()

    skills_query = " ".join(job_info["SKILLS"])

    st.subheader("📁 Indexing Resumes...")
    collection = init_resume_collection()

    for resume in resumes:
        text = extract_text_from_resume(resume)
        uid = str(uuid.uuid4())
        collection.add(documents=[text], ids=[uid])

    st.subheader("🎯 Matching Resumes...")
    results = collection.query(query_texts=[skills_query], n_results=top_k)

    top_resumes = ""
    st.success("✅ Top Matching Candidate Names:")
    for i, doc in enumerate(results["documents"], start=1):
        full_text = doc[0]
        lines = full_text.strip().splitlines()
        name = next((line for line in lines if line.strip()), "Unnamed Candidate")
        top_resumes += f"Candidate {i}: {name}\n"
        st.markdown(f"**Candidate {i}:** {name}")


    # top_resumes = "\n\n".join(["\n".join(doc) for doc in results["documents"]])
    # st.success("✅ Top Matching Resumes:")
    # for i, doc in enumerate(results["documents"], start=1):
    #     st.markdown(f"**Candidate {i}:**\n\n{doc[0]}")

    st.subheader("📧 Generating Email...")
    email_content = generate_email(top_resumes)
    st.code(email_content)

    st.download_button("📩 Download Email", email_content, file_name="shortlisted_email.txt")

