MODELS: dict[str, dict[str, str]] = {
    "llama3.2": {
        "Model": "`llama3.2`",
        "Description": "The Meta Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.",
        "Parameters": "3B",
        "Tools": "True",
    },
    "llama3.2:1b": {
        "Model": "`llama3.2:1b`",
        "Description": "The Meta Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.",
        "Parameters": "1B",
        "Tools": "True",
    },
    "deepseek-r1:1.5b": {
        "Model": "`deepseek-r1:1.5b`",
        "Description": "DeepSeek's first-generation reasoning models, achieving performance comparable to OpenAI-o1 across math, code, and reasoning tasks.",
        "Parameters": "1.5B",
        "Tools": "False",
    },
    "qwen2.5-coder:3b": {
        "Model": "`qwen2.5-coder:3b`",
        "Description": "Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, a range of base language models and instruction-tuned models are released, with sizes ranging from 0.5 to 72 billion parameters.",
        "Parameters": "3B",
        "Tools": "True",
    },
    "qwen2.5-coder:1.5b": {
        "Model": "`qwen2.5-coder:1.5b`",
        "Description": "Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, a range of base language models and instruction-tuned models are released, with sizes ranging from 0.5 to 72 billion parameters.",
        "Parameters": "1.5B",
        "Tools": "True",
    },
}


def create_model_table(
    models: dict[str, dict[str, str]] = MODELS,
    delimiter: str = "|",
) -> str:
    # Create a markdown table from the models
    model_table: str = ""
    # Construct header of table
    headers: list = []
    for model in models.values():
        headers = list(model.keys())
        break
    model_table += f"{delimiter}{delimiter.join(headers)}{delimiter}\n"
    for header in headers:
        model_table += f"{delimiter} --- "
    model_table += f"{delimiter}\n"
    # Construct value rows of table
    rows: list = []
    for model in models.values():
        row: list = []
        for value in model.values():
            row.append(value)
        rows.append(f"{delimiter}{delimiter.join(row)}{delimiter}")
    model_table += "\n".join(rows)
    return model_table


model_table: str = create_model_table()

TT_MODEL: str = f"""
A `Large Language Model` (LLM) is a type of artificial intelligence (AI) model trained on vast amounts of text data to understand and generate human-like text.
These models use deep learning techniques, specifically transformers, to process and generate language.
There are a lot of different models available nowadays.
Different models have unique strengths, architectures, and use cases.

These are the available models:

{model_table}
"""

TEMPLATES: dict[str, str] = {
    "RAG Assistant": """
Instruction:
You are a helpful chatbot assistant.
Answer the user's question using the provided document.
If the document doesn't contain the facts to answer the question,
let the user know the document isn't sufficient before answering the question.
Take the conversation history in consideration when answering the question.

Document:
{document}

Conversation history:
{chat_history}

Question:
{user_question}
""",
    "No Template": "",
}

TT_TEMPLATE: str = """
A `ChatPromptTemplate` is a tool in LangChain used to structure prompts for Large Language Models (LLMs).
It allows you to dynamically insert variables, format messages, and create structured multi-turn conversations for chat-based models.
"""

TEMPERATURE: dict[str, float] = {"min_value": 0.0, "max_value": 1.5, "step": 0.1}

TT_TEMPERATURE: str = """
`Temperature` is a parameter in Large Language Models (LLMs) that controls the randomness of their responses.
It affects how deterministic or creative the model's output is:

-   Lower temperatures results in more focused, deterministic, and factual responses.
-   Higher temperatures results in more creative, diverse, and random responses.

| Use Case                         | Temperature   |
| -------------------------------- | ------------- |
| Factual Answers                  | `0.1` - `0.3` |
| Code Generation                  | `0.2` - `0.5` |
| Brainstorming & Creative Writing | `0.7` - `1.2` |
| Open-Ended Conversations         | `0.6` - `1.0` |
| Poetry & Storytelling            | `0.9` - `1.5` |
"""
