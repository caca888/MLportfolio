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
[RAG essentials](https://github.com/caca888/MLportfolio/blob/main/rag/rag.py)
### Overview
This code implements a basic RAG system for processing and querying PDF documents. The system encodes the document content into a vetor store, which can be queried to retrieve relevant information.
### Key Components
1. User send a query
2. Document processing and text extraction are chunked for further steps
3. Vector store creation using FAISS and embedding to retrieve relevant document chunks
4. Retriever provides the relevant document chunks for context based on the query for LLM answering
5. LLM generates response
![RAG System](/img/rag.jpeg)

## RAG Optimizations
|Name|Description|Benefits|Link|
|---|---|---|---|
|Query Transformations for Improved Retrieval in RAG Systems | Three query transformation techniques: Query Rewriting, Step-back Prompting, and Sub-query Decomposition. | RAG sytems often face challenges in retrieving the most relevant information, especially when dealing with complex or ambiguous queries. These query transformation techniques address this issue by reformulating queries to better match relevant documents or to retrieve more comprehensive information.| [Query Transformations Implementation](https://github.com/caca888/MLportfolio/blob/main/rag/05_query_transformation.ipynb)
|
|Hypothetical Document Embedding (HyDE) in Document Retrieval | Hypothetical Document Embedding (HyDE) system  is an innovative approach that transforms query questions into hypothetical documents containing the answer, aiming to bridge the gap between query and document distributions in vector space. | Traditional retrieval method often stuggle with the semantic gap between short queries and longer, more detailed documents. | [HyDE Implementation](https://github.com/caca888/MLportfolio/blob/main/rag/06_hypothetical_Doc_Emb.ipynb) |
| Context Enrichment Window for Document Retrieval | Context enrichtment window technique enhances the standard retrieval process by adding surrounding context to each retrieved chunk, improving the coherence and completeness of the returned information | Traditional vector search often returns isolated chunks of text, which may lack necessary context for full understanding. This approach aims to provide a more comprehensive view of the retrieved information by including neighboring text chunks | [Context Enrichment Window](https://github.com/caca888/MLportfolio/blob/main/rag/07_context_enrichment.ipynb) |
| Semantic Chunking for Document Processing | Semantic chunking aims to create more meaningful and context-aware text segments | Traditional text splitting methods often break documents at arbitrary points, potentially disrupting the flow of information and context. Semantic chunking addresses this issue by attempting to split text at more natural breakpoints, preserving semantic coherence within each chunk | [Semantic Chunking for Document Processing](https://github.com/caca888/MLportfolio/blob/main/rag/08_semantic_chunking_document.ipynb) |
| Contextual Compression in Document Retrieval | Contextual compression  aims to improve the relevance and conciseness of retrieved information by compressing and extracting the most pertinent parts of documents in the context of a given query | Traditional document retrieval systems often return entire chunks or documents, which may contain irrelevant information. Contextual compression addresses this by interlligently extracting and compressing only the most relevant parts of retrieved documents, leading to more focused and efficient information retrieval | [Contextual Compression in Document Retrieval](https://github.com/caca888/MLportfolio/blob/main/rag/09_contextual_compression.ipynb) |
| Document Augmentation Through Question Generation for Enhanced Retrieval | By generating and incorporating various questions related to each text fragment, the system enhances the standard retrieval process, thus increasing the likelihood of finding relevant documents that can be utilized as context for generative question answering | By enriching text fragments with related questions, we aim to significantly enhance the accuracy of identifying the most relevant sections of a document that contain answers to user queries | [Document Augmentation Through Question Generation for Enhanced Retrieval](https://github.com/caca888/MLportfolio/blob/main/rag/10_Document_Augmentation.ipynb) |
| Hybrid Search | Fusion Retrieval system combines vector-based similarity search with keyword-based BM25 retrieval. The approach aims to leverage the strengths of both methods to improve the overall quality and relevance of document retrieval | Traditional retrieval methods often reply on either semantic understanding (vector-based) or keyword matching (BM25). Each appraoch has its strengths and weaknesses. Fusion retrieval aims to combine these methods to create a more robust and accurate retrieval system that can handle a wider range of queries effiectively | [Hybrid Search](https://github.com/caca888/MLportfolio/blob/main/rag/11_fusion_retrieval.ipynb) |
| Reranking | Reranking ims to improve the relevance and quality of retrieved documents. It involves reassessing and reordering initially retrieved documents to ensure that the most pertinent information is prioritized for subsequent processing or presentation | The primary motivation for reranking in RAG systems is to overcome limitations of initial retrieval methods, which often rely on simpler similarity metrics. Reranking allows for more sophisticated relevance assessment, taking into account nuanced relationships between queries and documents that might be msised by traditional retrieval techniques. This process aims to enhance the overall preformance of RAG systems by ensuring that the most relevant information is ues in the generation phase | [Reranking Methods in RAG systems](https://github.com/caca888/MLportfolio/blob/main/rag/12_reranking.ipynb) | 
| Hierarchical Indices in Document Retrieval | Hierarchical Indexing system utilizing two levels of encoding: document-level summaries and detailed chunks. This approach aims to improve the efficiency and relevance of information retrieval by fist identifying relevant documnent sections through summaries, then drilling down to specific details within those sections | Traditional flat indexing methods can struggle with large documents or corpus, potentially missing context or returning irrelevant information. Hierarchical indexing addresses this by creating a two-tier search system, allowing for more efficient and context-aware retrieval | [Hierarchical Indices](https://github.com/caca888/MLportfolio/blob/main/rag/13_hierarchical_indices.ipynb) | 
| RAG with Feedback Loop | This system aims to improve the quality and relevance of responses over time by incorporating user feedback and dynamically adjusting the retrieval process | Tranditional RAG systems can sometimes produce inconsistent or irrelevant responses due to limitations in the retrieval process or the underlying knowledge base. By implementing a feedback loop, we can Continuously improve the quality of retrieved documents, Enhance the relevance of generated responses, and Adapt the system to user preferences and needs over time | [RAG with Feedback Loop](https://github.com/caca888/MLportfolio/blob/main/rag/14_retrieval_with_feedback.ipynb) |

