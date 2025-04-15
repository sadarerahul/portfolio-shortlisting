import chromadb

def init_portfolios():
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="portfolios")
    collection.add(
        documents=[
            "Rahul is a Data Scientist with 2 years experience in ML, GenAI, and DL.",
            "Ramraje is a Python developer with 3 years experience, expert in ML.",
            "Soham specializes in cloud computing, ML, DL.",
            "Om is a web developer skilled in Python, HTML, Java, JavaScript."
        ],
        ids=["p1", "p2", "p3", "p4"]
    )
    return collection
