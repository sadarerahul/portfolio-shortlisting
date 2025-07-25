from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    api_key=groq_api_key
)


def extract_job_info(job_text: str) -> str:
    """
    Extract JOB_ROLE, EXPERIENCE, and SKILLS in JSON format using Groq LLM.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract JOB_ROLE, EXPERIENCE, SKILLS in JSON. No extra output."),
        ("human", "{input}")
    ])
    chain = prompt | llm

    if len(job_text) > 3000:
        job_text = job_text[:3000]  # Truncate long text for LLM

    result = chain.invoke({"input": job_text})
    return result.content
