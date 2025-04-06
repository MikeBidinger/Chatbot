# Chatbot

A (locally ran) LLM agnostic chatbot with both memory and RAG capabilities.
There is also the possibility to change specific parameters within the UI to influence behavior and results.
We'll break down the components one by one, each with an implementation example to follow along:

-   [Streamlit](#streamlit)
-   [LLM](#llm)
-   [LangChain](#langchain)
-   [RAG](#rag)
-   [Vector Store - ChromaDB](#vector-store---chromadb)

Before getting started, we first have to setup our virtual environment.
For more detailed information about virtual environments see the [venv documentation](https://github.com/MikeBidinger/Python_venv).

## Streamlit

The UI of this application is made using Streamlit.
Streamlit is an open-source Python library that makes it easy to create interactive web applications for machine learning, data visualization, and general-purpose apps.
For more detailed information about Streamlit visit their [homepage](https://streamlit.io/) or [documentation](https://docs.streamlit.io/).
For full chat and LLM app tutorials visit their [Build LLM apps](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps) tutorials.

See [1_streamlit.py](/1_streamlit.py) for an implementation example.
Use the following command in the CLI to run the script (make sure the current directory is correct):

```bash
streamlit run 1_streamlit.py
```

## LLM

The Large Language Models (LLMs) used are the Ollama models.
For more detailed information about Ollama see the [Ollama documentation](https://github.com/MikeBidinger/Ollama).

But with the use of LangChain the entire application is LLM agnostic.
This means that any LLM could be integrated without having to change the entire application.

See [2_llm.py](/2_llm.py) for an implementation example.
Use the following command in the CLI to run the script (make sure the current directory is correct):

```bash
python 2_llm.py
```

## LangChain

Utilizing LangChain will enable a LLm agnostic application.
Apart from this, we will also utilize the chain ability.
A chain refers to a sequence of components (like LLMs, prompt templates, memory, and tools) that work together to process an input and generate an output.
Chains allows us to build more structured, multi-step AI workflows rather than just calling an LLM directly.

See [3_langchain.py](/3_langchain.py) for an implementation example.
Use the following command in the CLI to run the script (make sure the current directory is correct):

```bash
python 3_langchain.py
```

## RAG

Retrieval Augmented Generation (RAG) is a technique that improves the performance of Large Language Models (LLMs) by combining retrieval (fetching relevant data) with generation (text generation by an LLM).
Instead of relying solely on the LLM’s pre-trained knowledge, RAG retrieves relevant external documents and uses them to generate more accurate and up-to-date responses.

See [4_rag.py](/4_rag.py) for an implementation example.
Use the following command in the CLI to run the script (make sure the current directory is correct):

```bash
python 4_rag.py
```
