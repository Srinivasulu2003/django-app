from django.shortcuts import render
from django.http import JsonResponse
import os
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain import hub
from langchain_cohere import ChatCohere
from langchain.schema import Document

# Set the API key for Cohere (use your own API key)
os.environ["COHERE_API_KEY"] = 'KP3KMGJEyBpbP2pBh0VJhbZNCvYDxeBVBBiZhtRX'
os.environ["HF_TOKEN"] = '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'

# Define function to create and run RAG model with simple text input
def run_rag_model_with_text(query, text, embeddings_model_name="sentence-transformers/all-MiniLM-L6-v2", llm_model="command-r-plus"):
    # Load the text as a document
    documents = [Document(page_content=text)]
    
    # Split the document into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)
    
    # Create embeddings using the HuggingFace model
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    
    # Create a vector store from document splits and the embedding model
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    
    # Retrieve the relevant information from the document
    retriever = vectorstore.as_retriever()
    
    # Load the RAG prompt template
    prompt = hub.pull("rlm/rag-prompt")
    
    # Initialize the LLM using Cohere
    llm = ChatCohere(model=llm_model)
    
    # Format the output content
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    # Establish the RAG chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Invoke the RAG chain with the query and return the result
    return rag_chain.invoke(query)

# Django view to handle chatbot queries
def chat(request):
    query = request.GET.get('message', '')
    
    # Example document (you can replace this with a database or external source)
    text = """
    - Product Name: SmartHome Thermostat
    - Purpose: To control and monitor home temperature automatically.
    - Features:
      - Energy-efficient heating and cooling management.
      - Wi-Fi connectivity for remote access via a mobile app.
      - Compatible with voice assistants like Alexa and Google Assistant.
      - Customizable temperature schedules.
      - Real-time energy usage tracking.
    - Target Audience: Homeowners looking to reduce energy bills and automate their home climate control.
    - Price: $199
    """
    
    if query:
        # Run the RAG model and get the result
        response = run_rag_model_with_text(query, text)
    else:
        response = "Please provide a query."

    # Return the response as JSON
    return JsonResponse({'response': response})

def index(request):
    return render(request, 'chatbot/index.html')
