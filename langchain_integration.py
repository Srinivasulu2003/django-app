from langchain.vectorstores import FAISS
from langchain.embeddings import CohereEmbeddings
from langchain.llms import Cohere
import cohere
cohere_client=cohere.Client("KP3KMGJEyBpbP2pBh0VJhbZNCvYDxeBVBBiZhtRX")
docs=[
    "productX is a cloud-based solution that automates bussiness workflows.",
    "productX integrates with existing Crms and provides real-time analytics.",
    "productx can handle up to 100 api request for second."
]

cohere_embeddings=CohereEmbeddings(cohere_api_keys="KP3KMGJEyBpbP2pBh0VJhbZNCvYDxeBVBBiZhtRX")
vector_store=FAISS.from_texts(docs,cohere_embeddings)
def answer_query(query):
    docs=vector_store.similarity_search(query)
    context="".join([doc.page_content for doc in docs])
    llm=Cohere(cohere_api_keys="KP3KMGJEyBpbP2pBh0VJhbZNCvYDxeBVBBiZhtRX")
    prompt=f"answer the question '{query}' based on this context{context}"
    response=llm(prompt)
    return response