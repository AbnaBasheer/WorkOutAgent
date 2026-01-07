import chromadb
from chromadb.utils import embedding_functions
import os

client = chromadb.Client()

embedding_function = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name = "fitness_knowledge",
    embedding_function = embedding_function
)

def load_knowledge(force_refresh=False):
    # If we want to refresh the database with new text from the file
    if force_refresh:
        ids_to_del = [f"doc_{i}" for i in range(collection.count())]
        if ids_to_del:
            collection.delete(ids=ids_to_del)

    if collection.count() > 0 and not force_refresh:
        return
    
    if not os.path.exists("data/knowledge.txt"):
        return

    with open("data/knowledge.txt", "r", encoding="utf-8") as f:
        docs = f.read().split("-" * 30) # Split by the separator used in scraper
        
    for i, doc in enumerate(docs):
        if doc.strip():
            collection.add(
                documents=[doc.strip()],
                ids=[f"doc_{i}"]
            )
        
def retrieve_context(query, k=5):
    results = collection.query(
        query_texts = [query],
        n_results = k
    )
    
    return "\n".join(results["documents"][0])