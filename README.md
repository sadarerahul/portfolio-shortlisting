🌐 Live Demo =https://portfolio-shortlisting.onrender.com/
# 💼 Portfolio Shortlisting System using RAG & Generative AI

An intelligent resume shortlisting system powered by LLMs and Retrieval-Augmented Generation (RAG) — built to help job consultancies and recruiters find the best candidate matches quickly from a batch of resumes.

![Streamlit UI](https://img.shields.io/badge/Streamlit-Enabled-green) ![LLM Powered](https://img.shields.io/badge/GenerativeAI-LLM-blue) ![License](https://img.shields.io/github/license/sadarerahul/portfolio-shortlisting)

---

## 🚀 Features

- ✅ Upload any Job Description (JD) & Resume folder (PDF/DOCX)
- 🔍 Uses advanced embeddings to compare candidate skills with job requirements
- 🧠 Powered by **RAG (Retrieval-Augmented Generation)** using **Groq LLM**
- 📂 Returns top N matching resumes based on semantic similarity
- 💌 Auto-generates recruiter summary and email content using LLMs
- 📱 Clean, interactive **Streamlit** web UI
- 🧠 Uses **LangChain**, **ChromaDB**, and **langchain_groq**

---

## 📁 Project Structure


---

## 📷 Screenshots

| Upload Job & Resumes         | Matching Candidate Profiles       |
|-----------------------------|-----------------------------------|
| ![upload](screenshots/upload.png) | ![matches](screenshots/matches.png) |

---

## 🧠 How It Works

1. 📤 Upload a Job Description (JD) and a folder of resumes
2. 📖 Resumes are embedded and stored in a **ChromaDB**
3. 🔎 JD is converted to query and compared using **semantic search**
4. 🏆 Top N resumes are shortlisted based on similarity
5. 🤖 LLM generates email response + summary using **Groq (LLM API)**

---

## 🛠️ Tech Stack

| Component      | Tool |
|----------------|------|
| Frontend       | Streamlit |
| Backend Logic  | Python |
| AI/LLM         | Groq API via `langchain_groq` |
| Vector DB      | ChromaDB |
| RAG Framework  | LangChain |
| File Handling  | PyMuPDF / python-docx |
| Hosting        | Render / Hugging Face Spaces (optional) |

---

## 🧪 Local Setup

```bash
# Step 1: Clone this repo
git clone https://github.com/sadarerahul/portfolio-shortlisting.git
cd portfolio-shortlisting

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app.py


 Author
Sada Rahul
🎓 BSc Computer Science | Data Science Enthusiast
🔗 LinkedIn
📧 sadarerahul@example.com


⭐ Acknowledgements
LangChain

Streamlit

ChromaDB

Groq API
