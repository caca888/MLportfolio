[![Makefile CI](https://github.com/caca888/MLportfolio/actions/workflows/makefile.yml/badge.svg)](https://github.com/caca888/MLportfolio/actions/workflows/makefile.yml)

# Porfolio Demo 

## Setup with Devlopment environment

* create virutal environment ```virtualenv ~/.venv```
* run the virtual environment ```source ~/.venv/bin/activate```
* add the virtual environment to bash shell ```vim ~/.bashrc```
* create Makefile ```touch Makefile```
* create requirements.txt ```touch requirements.txt```
* create source directory ```mkdir src``` with ```__init__.py``` for package include
* create test directory ```mkdir test```


## CI Environment

![CI Environment](/img/CI.PNG)

## RAG
### Overview
This code implements a basic RAG system for processing and querying PDF documents. The system encodes the document content into a vetor store, which can be queried to retrieve relevant information.
### Key Components
1. PDF processing and text extraction
2. Text chunking for manageable processing
3. Vector store creation using FAISS and OpenAI embedding
4. Retriever setup for querying the processed documents
5. Evaluation of the RAG system
### Details
#### Document Preprocessing
1. PDF is loaded using PyPDFLoader
2. The text is split into chunks using RecursiveCharacterTextSplitter with specified chunk size and overlap
#### Text Cleaning
`replace_t_with_space` is applied to clean the text chunks. 
#### Vector Store Creation
1. OpenAI embeddings are used to create vector representations of the text chunks.
2. FAISS vector store is created from these embeddings for efficient similarity serach.
#### Retriever Setup
1. Retriever is configured to fetch the top 2 most relevant chunks for a given query.
#### Encoding Function
`encode_pdf` function encapsulates the entire process of loading, chunking, cleaning and encoding the PDF into a vector store.