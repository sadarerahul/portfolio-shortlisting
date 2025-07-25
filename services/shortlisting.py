import json, uuid, re
from services.llm_utils import extract_job_info
from services.email_generator import generate_email
from services.portfolios import init_resume_collection
from services.resume_utils import extract_text_from_resume

def clean_json_response(raw_text: str):
    import re
    clean_text = re.sub(r"```json|```", "", raw_text).strip()
    try:
        return json.loads(clean_text)
    except json.JSONDecodeError:
        return {"JOB_ROLE": "", "EXPERIENCE": "", "SKILLS": []}

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else "Not Available"

def shortlist_candidates(job_post_text, resume_files, top_k=3, company_name="Company"):
    job_info_json = extract_job_info(job_post_text)
    job_info = clean_json_response(job_info_json)
    skills_query = " ".join(job_info.get("SKILLS", []))

    collection = init_resume_collection()

    # ✅ Store extracted text for mapping later
    for rf in resume_files:
        text = extract_text_from_resume(rf["file"])
        uid = str(uuid.uuid4())
        collection.add(documents=[text], ids=[uid])
        rf["text"] = text

    results = collection.query(query_texts=[skills_query], n_results=top_k)

    candidates = []
    for docs in results["documents"]:  # ✅ Loop over each list of docs
        for full_text in docs:  # ✅ Extract all docs in case of duplicates
            lines = full_text.strip().splitlines()
            name = next((line for line in lines if line.strip()), "Unnamed Candidate")
            email = extract_email(full_text)

            # ✅ Improved robust file matching
            matched_resume = None
            for rf in resume_files:
                if rf["text"][:100] in full_text or full_text[:200] in rf["text"]:
                    matched_resume = rf["path"]
                    break

            candidates.append({
                "name": name,
                "email": email,
                "file": matched_resume
            })

    # ✅ Limit to top_k only (in case extra matches found)
    candidates = candidates[:top_k]

    top_resumes_text = "\n".join([f"{c['name']} - {c['email']}" for c in candidates])
    email_content = generate_email(top_resumes_text, company_name)

    return {"candidates": candidates, "email": email_content}
