"""
RAG Evaluation Script

This script evaluates the performance of a Retrieval-Augmented Generation (RAG) system
using various metrics from the deepeval library.

Dependencies:
- deepeval
- json

Custom modules:
- helper_functions (for RAG-specific operations)
"""

import json
from typing import List, Tuple

from deepeval import evaluate
from deepeval.metrics import GEval, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from langchain_openai.chat_models.azure import AzureChatOpenAI
import sys
import os


openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
openai_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID")
openai_api_version = os.getenv("AZURE_API_VERSION")
aws_region = os.getenv("AWS_REGION")
aws_titan_model = os.getenv("AWS_TITAN_MODEL")
aws_titan_max_token = os.getenv("AWS_TITAN_MAX_TOKEN")
aws_titan_temperature = os.getenv("AWS_TITAN_TEMPERATURE")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from helper_functions import (
    answer_question_from_context,
    create_question_answer_from_context_chain,
    retrieve_context_per_question
)


    

def create_deep_eval_test_case(
        questions: List[str],
        gt_answers: List[str],
        generated_answers: List[str],
        retrieved_documents: List[str]
) -> List[LLMTestCase]:
    """
    Create a list of LLMTestCase objects for evaluation.

    Args:
        questions (List[str]): List of input questions.
        gt_answers (List[str]): List of ground truth answers.
        generated_answers (List[str]): List of generated answers.
        retrieved_documents (List[str]): List of retrieved documents.

    Returns:
        List[LLMTestCase]: List of LLMTestCase objects.
    """

    return [
        LLMTestCase(input=question, expected_output=gt_answer, actual_output=generated_answer, retrieval_context=retrieved_document)
        for question, gt_answer, generated_answer, retrieved_document in zip(questions, gt_answers, generated_answers, retrieved_documents)
    ]



correct_metric = GEval(
    name="Correctness",
    model="gpt-4o",
    evaluation_params=[
        LLMTestCaseParams.EXPECTED_OUTPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT
    ],
    evaluation_steps=[
        "Determine whether the actual output is factually correct based on the expected output."
    ],
)


faithfulness_metric = FaithfulnessMetric(
    threshold=0.7,
    model="gpt-4o",
    include_reason=False
)

relevance_metric = ContextualRelevancyMetric(
    threshold=1,
    model="gpt-4o",
    include_reason=True
)

def evaluate_rag(chunks_query_retriever, num_question: int = 1) -> None:
    """
    Evaluate the RAG system using predefined metrics.

    Args:
        chunks_query_retriever: Function to retrieve context chunks for a given query.
        num_questions (int): Number of questions to evaluate (default: 5).
    """
    llm = AzureChatOpenAI(
        azure_deployment=openai_deployment,
        api_version="2024-10-01-preview",
        azure_endpoint=f"{openai_endpoint}openai/deployments/{openai_deployment}/chat/completions?api-version=2024-10-01-preview",
        temperature=0,
        logprobs=True,
    )

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to German. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)

    question_answer_from_context_chain = create_question_answer_from_context_chain(llm)

    # Load questions and answers from JSON file
    q_a_file_name = "./data/q_a.json"
    with open(q_a_file_name, "r", encoding="utf-8") as json_file:
        q_a = json.load(json_file)

    questions = [qa["question"] for qa in q_a][:num_question]
    ground_truth_answers = [qa["answer"] for qa in q_a][:num_question]

    generated_answers = []
    retrieved_documents = []

    # Generate answers an dretrieve documents for each question
    for question in questions:
        context = retrieve_context_per_question(question=question, chunks_query_retriever=chunks_query_retriever)
        retrieved_documents.append(context)
        context_string = " ".join(context)
        result = answer_question_from_context(question=question, context=context_string, question_answer_from_context_chain=question_answer_from_context_chain)
        generated_answers.append(result["answer"])

    # Create test cases and evaluate
    test_cases = create_deep_eval_test_case(questions=questions, gt_answers=ground_truth_answers, generated_answers=generated_answers, retrieved_documents=retrieved_documents)

    evaluate(test_cases=test_cases, metrics=[correct_metric, faithfulness_metric, relevance_metric])


if __name__ == "__main__":
    # Add any necessary setup or configuration here
    # Example: evaluate_rag(your_chunks_query_retriever_function)
    pass