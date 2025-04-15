import streamlit as st
import json
from llm_utils import extract_job_info
from portfolios import init_portfolios
from email_generator import generate_email


from dotenv import load_dotenv
import os

load_dotenv()  # This will load the environment variables from .env file

# Then access your API key like this:
groq_api_key = os.getenv("GROQ_API_KEY")

import chromadb

# Initialize Chroma client
chroma_client = chromadb.Client()

# Create or get the collection
collection = chroma_client.get_or_create_collection(name="my_collection1")





st.set_page_config(page_title="Portfolio Shortlisting with LLM", layout="centered")

st.title("🧠 Portfolio Shortlisting using RAG + LLM")

# Upload job description
job_file = st.file_uploader("Upload Job Description", type=["txt", "pdf", "docx"])

if job_file:
    job_text = job_file.read().decode("utf-8", errors="ignore")

    st.subheader("📄 Extracting Job Info...")
    job_info_json = extract_job_info(job_text)

    try:
        job_info = json.loads(job_info_json.strip("`\n"))
        st.json(job_info)
    except Exception as e:
        st.error("Failed to extract job details. Try again.")
        st.stop()

    skills_query = " ".join(job_info["SKILLS"])

    st.subheader("🔍 Matching Portfolios...")
    collection = chroma_client.get_or_create_collection(name="my_collection1")

    results = collection.query(query_texts=[skills_query], n_results=2)
    top_portfolios = " ".join(results["documents"][0])

    st.success("✅ Shortlisted Candidates:")
    for doc in results["documents"]:
        st.write(doc)

    st.subheader("📧 Generating Email...")
    email_content = generate_email(top_portfolios)
    st.code(email_content)

    st.download_button("📥 Download Email", email_content, file_name="shortlist_email.txt")

