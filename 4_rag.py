from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable
from langchain_core.messages import HumanMessage, AIMessage

MODEL: str = "llama3.2"
TEMPERATURE: float = 0.0
TEMPLATE: str = """
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
"""
FILE_PATH: str = "./rag_data/doc.md"


def get_response(user_prompt, chat_history, document) -> str:
    # Create chain
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(template=TEMPLATE)
    llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)
    chain: RunnableSerializable = prompt | llm | StrOutputParser()
    # Invoke chain
    return chain.invoke(
        {
            "chat_history": chat_history,
            "user_question": user_prompt,
            "document": document,
        }
    )


chat_history: list = []

documentation: str = ""
with open(FILE_PATH, "r") as f:
    documentation = f.read()

print("Enter your question or enter 'q' to quit.")

while True:

    # User input
    user_prompt: str = input("You: ")

    if user_prompt.lower() == "q":
        break

    elif user_prompt:
        chat_history.append(HumanMessage(user_prompt))

        response: str = get_response(user_prompt, chat_history, documentation)
        print(response)

        chat_history.append(AIMessage(response))

quit()
