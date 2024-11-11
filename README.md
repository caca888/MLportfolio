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

## Query Transformations for Improved Retrieval in RAG Systems
### Overview
This code implements three query transformation techniques to enhance the retrieval process in RAG systems:
1. Query Rewriting
2. Step-back Prompting
3. Sub-query Decomposition
Each technique aims to improve the relevance and comprehensiveness of retrieved information by modifying or expanding the original query.
### Motivation
RAG sytems often face challenges in retrieving the most relevant information, especially when dealing with complex or ambiguous queries. These query transformation techniques address this issue by reformulating queries to better match relevant documents or to retrieve more comprehensive information.
### Key Components
1. Query Rewriting: Reformulates queries to be more specific and detailed.
2. Step-back Prompting: Generates broader queries for better context retrieval.
3. Sub-query Decomposition: Breaks down complex queries into simpler sub-quries.
### Method Details
#### Query Rewriting
- Purpose: To make queries more specific and detailed, improving the likelihood of retrieving relevant information
- Implementation:
    * Uses a GPT-4 model with a custom prompt template
    * Takes the original query and reformulates it to be more specific and detailed
#### Step-back Prompting
- Purpose: To generate broader, more general queries that can help retrieve relevant background information
- Implementation:
    * Uses a GPT-4 model with a custom prompt template
    * Takes the original query and generates a more general "step-back" query
#### Sub-query Decomposition
- Purpose: To break down complex queries into simpler sub-queries for more comprehensive information retrieval
- Implementation:
    * Uses a GPT-4 model with a custom prompt template
    * Decomposes the original query into 2-4 simpler sub-queries
### Benefits of these Approaches
1. Improved Relevance: Query rewriting helps in retrieving more specifc and relevant information
2. Better Context: Step.back prompting allows for retrieval of broader context and background information
3. Comprehensive Results: Sub-query decomposition enables retrieval of information that covers different aspects of a complex query
4. Flexibility: Each technique can be used independently or in combination, depending on the specific use case
### Example Use Case
The code demonstrates each technique using the example query "What are the impacts of climate change on the environment?"
- Query Rewriting expands this to include specific aspects like temperature changes and biodiversity
- Step-back Prompting generalizes it to "What are the general effects of climate change?"
- Sub-query Decomposition breaks it down into questions about biodiversity, oceans, weather patterns, and terrestrial environments
### Conclusion
These query transformation techniques offer powerful ways to enhance the RAG systems. By reformulating queries in various ways, they can significantly improve the relevance, context and comprehensiveness of retrieved information. These methods are particularly valuable in domains where queries can be complex or multifaceted., such as scientific research, leagal analysis or comprehensive fact-finding tasks.

## Hypothetical Document Embedding (HyDE) in Document Retrieval
### Overview
This code implements a Hypothetical Document Embedding (HyDE) system for document retrieval. HyDE is an innovative approach that transforms query questions into hypothetical documents containing the answer, aiming to bridge the gap between query and document distributions in vector space.
### Movtivation
Traditional retrieval method often stuggle with the semantic gap between short queries and longer, more detailed documents. HyDE addresses this by expanding the query into a full hypothetical document, potentially improving retrieval relevance by making the query respresntation more similar to the document representation in the vector space.
### Key Components
1. PDF processing and text chunking
2. Vector store creation using FAISS and OpenAI embeddings
3. Language model for generating hypothetical documetns
4. Custom HyDEretriever class implementing the HyDE technique
### Method Details
#### Docuemnt Preprocessing and Vector Store Creation
1. The PDF is processed and split into chunks
2. A FAISS vector store is created using OpenAI Embeddings for efficient similarity serach
#### Hypothetical Document Generation
1. A langugage model is used to generate a hypothetical document that answers the given query
2. The generation is guided by a prompt template that ensures the hypothetical document is detailed and matches the chunk size used in the vector store.
#### Retrieval Process
The `HyDERetriever` calss implements the following steps:
1. Generate a hypothetical document from the query using the language model
2. use the hypothetical document as the search query in the vector store
Retrieve the most similar documents to this hypothetical document
### Key Features
1. Query Expansion: Transforms short queries into detailed hypothetical documents
2. Flexible Configuration: Allows adjustment of chunk size, overlap, and number of retrieved documents
3. Integration with OpenAI models for hypothetical document generation and embeddings for vector representation
### Benefits of this Approach
1. Improved Relevance: By expanding queries into full documents, HyDE can potentailly capture more nuanced and relevant matches
2. Handling Complex Queries: Particularly useful for complex or multi-faced queries that might be difficult to match directly
3. Adaptability: The hypothetical document generation can adapt to different types of queries and document domains
4. Potential for Better Context Understanding: The expanded query might better capture the context and intent behind the original question
### Conclusion
HyDE represents an innovative approach to document retrieval, addressing the semantic gap between queries and documents. By leveraging advanced langugage models to expand queries into hypothetical documents. HyDE has the potential to significantly improve retrieval relevance, especially for coplex or nuanced queries. This technique could be particularly valuable in domains where understanding query intent and context is crucial.