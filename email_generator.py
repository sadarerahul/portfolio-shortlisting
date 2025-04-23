from langchain_core.prompts import ChatPromptTemplate
from llm_utils import llm

def generate_email(portfolios_text):
    email_prompt = ChatPromptTemplate.from_messages([
        ("system", '''We are placement officers at CodeSpyder. Based on the TCS job post, we've shortlisted candidates. Generate a formal email to TCS's hiring team with the shortlisted candidate information.'''),
        ("human", "{input}")
    ])
    email_chain = email_prompt | llm
    result = email_chain.invoke({"input": portfolios_text})
    return result.content

