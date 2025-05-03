from typing import Literal
from langgraph.func import entrypoint, task
from litellm import completion

# Define task types
TaskType = Literal["math", "writing", "coding"]
api_key= "your_api_key_here"  # Replace with your actual API key

@task
def classify_task(query: str) -> TaskType:
    """Task to classify the input into one of the predefined task types."""
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=api_key,
        messages=[{
            "role": "user",
            "content": f"""Given the following input, classify it as either 'math', 'writing', or 'coding'.
Only respond with one of these exact words.

Input: {query}
"""
        }]
    )
    return response.choices[0].message.content.strip().lower()

@task
def handle_math(query: str) -> str:
    """Task to handle mathematical queries."""
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=api_key,
        messages=[{
            "role": "user",
            "content": f"""You are a mathematical expert. Solve the following problem:
{query}
"""
        }]
    )
    return response.choices[0].message.content

@task
def handle_writing(query: str) -> str:
    """Task to handle writing queries."""
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=api_key,
        messages=[{
            "role": "user",
            "content": f"""You are a professional writer. Help with the following writing task:
{query}
"""
        }]
    )
    return response.choices[0].message.content

@task
def handle_coding(query: str) -> str:
    """Task to handle coding problems."""
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=api_key,
        messages=[{
            "role": "user",
            "content": f"""You are an expert programmer. Help with the following coding task:
{query}
"""
        }]
    )
    return response.choices[0].message.content

@entrypoint()
def router(query: str) -> str:
    """Entrypoint that routes the query to the appropriate task based on classification."""
    # Execute classification task synchronously
    task_type = classify_task(query).result()
    
    # Direct the flow based on the classified task type
    if task_type == "math":
        return handle_math(query["query"]).result()
    elif task_type == "writing":
        return handle_writing(query["query"]).result()
    elif task_type == "coding":
        return handle_coding(query["query"]).result()
    else:
        return "Could not classify the query type."

def main():
    obj = router.invoke({"query": "Write an essay about the benefits of AI of 100 words"})
    print(obj)
