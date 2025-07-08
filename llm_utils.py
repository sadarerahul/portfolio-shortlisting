from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


from dotenv import load_dotenv
import os

load_dotenv()  # This will load the environment variables from .env file

# Then access your API key like this:
groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq



llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    api_key=groq_api_key
)

def extract_job_info(job_text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract JOB_ROLE, EXPERIENCE, SKILLS in JSON. No extra output."),
        ("human", "{input}")
    ])
    chain = prompt | llm
    if len(job_text) > 3000:
        job_text = job_text[:3000]
    result = chain.invoke({"input": job_text})
    return result.content
