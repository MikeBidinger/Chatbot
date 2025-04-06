import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from langchain_core.messages import HumanMessage, AIMessage

MODELS: list[str] = [
    "llama3.2",
    "llama3.2:1b",
    "qwen2.5-coder:3b",
    "qwen2.5-coder:1.5b",
]

# App config
st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")
st.title("Chatbot")

# Sidebar
with st.sidebar:
    st.title("Settings")
    container: DeltaGenerator = st.container(border=True)
    container.header("LLM")
    model: str = container.selectbox(
        "Model Selection",
        MODELS,
    )
    temperature: float = container.slider(
        label="Temperature Selection",
        min_value=0.0,
        max_value=1.0,
        step=0.1,
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

prompt: str | None = st.chat_input("Enter your question here...")

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append(HumanMessage(prompt))

    response: str = f"Echo: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append(AIMessage(response))
