import os
import sys
from helper_functions import *

from evaluation.evalute_rag import *
from dotenv import load_dotenv


load_dotenv()

def encode_pdf(path, chunk_size=1000, chunk_overlap=200):
    """
    Encodes a PDF book into a vector store using OpenAI embeddings.

    Args:
        path: The path to the PDF file.
        chunk_size: The desired size of each text chunk.
        chunk_overlap: The amount of overlap between consecutive chunks.

    Returns:
        A FAISS vector store containing the encoded book content.
    """

    # Load PDF documents
    loader = PyPDFLoader(path)
    documents = loader.load()


    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    texts = text_splitter.split_documents(documents)

    cleaned_texts = replace_t_with_space(texts)
    openai_embedding = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_ID")

    # embeddings = get_langchain_embedding_provider(EmbeddingProvider.AZURE)
    from langchain_openai.embeddings.azure import AzureOpenAIEmbeddings
    embeddings = AzureOpenAIEmbeddings(
        deployment=openai_embedding,
        model="text-embedding-ada-002",
        chunk_size=16
    )
    vectorstore = FAISS.from_documents(cleaned_texts, embeddings)

    return vectorstore

def file_processing():
    path = "./data/Understanding_Climate_Change.pdf"

    chunks_vector_store = encode_pdf(path, chunk_size=1000, chunk_overlap=200)
    chunks_query_retriever = chunks_vector_store.as_retriever(search_kwargs={"k": 2})

    evaluate_rag(chunks_query_retriever=chunks_query_retriever)


if __name__=="__main__":
    file_processing()