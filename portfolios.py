import chromadb

def init_resume_collection():
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="resume_collection")
    return collection
