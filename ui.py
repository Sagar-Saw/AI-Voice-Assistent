# ui.py — Streamlit-based web interface for the AI Voice Assistant

import streamlit as st
from stt import take_voice_input
from llm import generate_response, clear_history
from tts import speak_text

st.set_page_config(page_title="AI Voice Assistant", page_icon="", layout="centered")

st.title("AI Voice Assistant")
st.markdown("**Speak in English or Hindi!**")
st.divider()

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

col1, col2 = st.columns(2)

with col1:
    if st.button("Speak Now", use_container_width=True):
        with st.spinner("Listening..."):
            user_input = take_voice_input()

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            with st.spinner("Thinking..."):
                ai_response = generate_response(user_input)

            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            speak_text(ai_response)
            st.rerun()
        else:
            st.warning("Could not understand. Please try again.")

with col2:
    if st.button("Clear Chat", use_container_width=True):
        # Reset both UI history and LLM conversation memory
        st.session_state.messages = []
        clear_history()
        st.rerun()

st.divider()

# Accept typed input as an alternative to voice
user_text = st.chat_input("Or type your message here...")

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})

    with st.spinner("Thinking..."):
        ai_response = generate_response(user_text)

    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    speak_text(ai_response)
    st.rerun()