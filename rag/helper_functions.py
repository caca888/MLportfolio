from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from openai import RateLimitError
from typing import List
from rank_bm25 import BM25Okapi
import fitz
import asyncio
import random
import textwrap
import numpy as np


def replace_t_with_space(list_of_documents):
    """
    Replaces all tab characters ('\t') with spaces in the page content of each document.
    
    Args:
        list_of_documents: A list of doument objects, each with a 'page_content' attribute.

    Returns:
        The modified list of documents with tab characters replaced by spaces.
    """
    for document in list_of_documents:
        if hasattr(document, 'page_content'):
            document.page_content = document.page_content.replace('\t', ' ')
        else:
            raise AttributeError(f"Document {document} does not have a 'page_content' attribute.")
    return list_of_documents


def create_question_answer_from_context_chain(llm):
    # Initialize the ChatOpenAI model with specific parameters
    question_answer_from_context_llm = llm

    # Define the prompt template for chain-of-thought reasoning
    question_answer_prompt_template = """
    For the question below, provide a concise but suffice answer based ONLY on the provided context:
    {context}
    Question
    {question}
    """

    # Create a PromptTemplate object with the specified template and input variables
    question_answer_from_context_prompt = PromptTemplate(
        template=question_answer_prompt_template,
        input_variables=["context", "question"],
    )

    # Create a chain by combining the prompt template and the language model
    question_answer_from_context_cot_chain = question_answer_from_context_prompt | question_answer_from_context_llm.with_structured_output (QuestionAnswerFromContext)


    return question_answer_from_context_cot_chain

def answer_question_from_context(question, context, question_answer_from_context_chain):
    """
    Answer a question using the given context by involking a chain of reasoning.

    Args: 
        question: The question to be answered.
        context: The context to be used for answering the question.

    Returns:
        A dictionary containing the answer, context, and question
    """
    input_data = {
        "question": question,
        "context": context
    }


    print("Answering the question from the retrieved context...")

    output = question_answer_from_context_chain.invoke(input_data)
    answer = output.answer_based_on_content

    return {"answer": answer, "context": context, "question": question}


def retrieve_context_per_question(question, chunks_query_retriever):
    """
    Retrieves relevant context and unique URLs fro a given question using the chunks query retriever.

    Args:
        question: The question for which to retrieve context and URLs.

    Returns:
        A tuple containing:
        - A string with the concatenated content of relevant documents.
        - A list of unique URLs from the metadata of the relevant documents.
    """
    # Retrieve relevant documents for the given question
    docs = chunks_query_retriever.invoke(question)

    # Concatenate document content
    context = [doc.page_content for doc in docs]

    return context


def show_context(context):
    """
    Display the contents of the provided context list.

    Args:
        context (list): A list of context items to be displayed.

    Prints each context item in the list with a heading indicating its position.
    """
    for i, c in enumerate(context):
        print(f"Context {i + 1}:")
        print(c)
        print("\n")



class QuestionAnswerFromContext(BaseModel):
    """
    Model to generate an answer to a query based on a given context.
    
    Attributes:
        answer_based_on_content (str): The generated answer based on the context.
    """
    answer_based_on_content: str = Field(description="Generates an answer to a query based on a given context.")