import pinecone
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

def get_vectorstore(api_key: str, environment: str, index_name: str, embeddings, namespace: str):
    pinecone = Pinecone(api_key=api_key, environment=environment)
    index = pinecone.Index(index_name)

    print("hay vectores cargados?")
    print(index.describe_index_stats())

    return PineconeVectorStore(index=index, embedding=embeddings, text_key="text", namespace=namespace)