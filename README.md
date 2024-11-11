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
[RAG Implementation](https://github.com/caca888/MLportfolio/blob/main/rag/rag.py)
### Overview
This code implements a basic RAG system for processing and querying PDF documents. The system encodes the document content into a vetor store, which can be queried to retrieve relevant information.
### Key Components
1. PDF processing and text extraction
2. Text chunking for manageable processing
3. Vector store creation using FAISS and OpenAI embedding
4. Retriever setup for querying the processed documents
5. Evaluation of the RAG system


## Query Transformations for Improved Retrieval in RAG Systems
[Query Transformations Implementation](https://github.com/caca888/MLportfolio/blob/main/rag/05_query_transformation.ipynb)

### Overview
This code implements three query transformation techniques to enhance the retrieval process in RAG systems:
1. Query Rewriting
2. Step-back Prompting
3. Sub-query Decomposition
Each technique aims to improve the relevance and comprehensiveness of retrieved information by modifying or expanding the original query.
### Motivation
RAG sytems often face challenges in retrieving the most relevant information, especially when dealing with complex or ambiguous queries. These query transformation techniques address this issue by reformulating queries to better match relevant documents or to retrieve more comprehensive information.

### Benefits of these Approaches
1. Improved Relevance: Query rewriting helps in retrieving more specifc and relevant information
2. Better Context: Step.back prompting allows for retrieval of broader context and background information
3. Comprehensive Results: Sub-query decomposition enables retrieval of information that covers different aspects of a complex query
4. Flexibility: Each technique can be used independently or in combination, depending on the specific use case


## Hypothetical Document Embedding (HyDE) in Document Retrieval
[HyDE Implementation](https://github.com/caca888/MLportfolio/blob/main/rag/06_hypothetical_Doc_Emb.ipynb)
### Overview
This code implements a Hypothetical Document Embedding (HyDE) system for document retrieval. HyDE is an innovative approach that transforms query questions into hypothetical documents containing the answer, aiming to bridge the gap between query and document distributions in vector space.
### Movtivation
Traditional retrieval method often stuggle with the semantic gap between short queries and longer, more detailed documents. HyDE addresses this by expanding the query into a full hypothetical document, potentially improving retrieval relevance by making the query respresntation more similar to the document representation in the vector space.

### Benefits of this Approach
1. Improved Relevance: By expanding queries into full documents, HyDE can potentailly capture more nuanced and relevant matches
2. Handling Complex Queries: Particularly useful for complex or multi-faced queries that might be difficult to match directly
3. Adaptability: The hypothetical document generation can adapt to different types of queries and document domains
4. Potential for Better Context Understanding: The expanded query might better capture the context and intent behind the original question
