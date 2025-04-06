from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable
from langchain_core.messages import HumanMessage, AIMessage, AnyMessage

MODEL: str = "llama3.2"
TEMPERATURE: float = 0.0
TEMPLATE: str = """
Give short and precise answers to the questions.

Here is the chat history: {chat_history}

Here is the question: {user_question}
"""


def get_response(user_prompt: str, chat_history: list[AnyMessage]) -> str:
    # Create chain
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(template=TEMPLATE)
    llm = ChatOllama(model=MODEL, temperature=0.0)
    chain: RunnableSerializable = prompt | llm | StrOutputParser()
    # Invoke chain
    return chain.invoke(
        {
            "chat_history": chat_history,
            "user_question": user_prompt,
        }
    )


chat_history: list = []

print("Enter your question or enter 'q' to quit.")

while True:

    # User input
    user_prompt: str = input("You: ")

    if user_prompt.lower() == "q":
        break

    elif user_prompt:
        chat_history.append(HumanMessage(user_prompt))

        response: str = get_response(user_prompt, chat_history)
        print(response)

        chat_history.append(AIMessage(response))
