from langchain_core.prompts import ChatPromptTemplate
from llm_utils import llm

def generate_email(portfolios_text):
    email_prompt = ChatPromptTemplate.from_messages([
        ("system", '''We are placement officers at CodeSpyder. Based on the specific job post, we've shortlisted candidates. Generate a formal email to company hiring team with the shortlisted candidate contact and basic information.'''),
        ("human", "{input}")
    ])
    email_chain = email_prompt | llm
    result = email_chain.invoke({"input": portfolios_text})
    return result.content

