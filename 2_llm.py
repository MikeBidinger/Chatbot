from langchain_ollama import ChatOllama

# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

MODEL: str = "llama3.2"
TEMPERATURE: float = 0.0


def get_response(user_prompt: str) -> str | list:
    # Load the local Ollama model
    llm = ChatOllama(model=MODEL, temperature=0.0)
    # llm = ChatOpenAI(model="gpt-4o-mini")  # Load the OpenAI model
    # llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")  # Load the Anthropic model
    return llm.invoke(user_prompt).content


print("Enter your question or enter 'q' to quit.")

while True:

    # User input
    user_prompt: str = input("You: ")

    if user_prompt.lower() == "q":
        break

    elif user_prompt:
        response: str | list = get_response(user_prompt)
        print(response)
