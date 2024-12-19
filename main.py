import streamlit as st
from chat_handler import get_bot_response
import time

# Page Configuration
st.set_page_config(page_title="Eywa - AI Support Agent", layout="centered", initial_sidebar_state="collapsed")

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Company Logo
st.markdown(
    """
    <div style="text-align: center; margin-left: 100px">
        <img src="https://massmutualventures.com/wp-content/uploads/testsigma-header-logo.png" alt="Company Logo" style="width: 500px;" />
    </div>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 class='title'>Eywa - AI Support Agent</h1>", unsafe_allow_html=True)

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Display Area
chat_container = st.empty()  # Placeholder for the chat container

def render_chat():
    """Function to render chat messages dynamically."""
    with chat_container.container():
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(
                    f"""
                    <div class="chat user">
                        <div class="bubble gradient-border">{message['content']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <img src = "https://avatars.githubusercontent.com/u/59315465?s=200&v=4" style="width: 20px;">
                    <div class="chat bot">
                        <div class="bubble bot-bubble">{message['content']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

# Input Box at Bottom
with st.form("user_input_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your message...", label_visibility="collapsed")
    submit = st.form_submit_button("Send")

# Handling user input and bot response
if submit and user_input:
    # Add user's message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    render_chat()  # Render chat with the user's message immediately

    # Placeholder for bot's response
    bot_response_placeholder = st.empty()

    # Generate the bot's response line by line
    with st.spinner("Eywa is typing..."):
        bot_reply = get_bot_response(user_input)  # Get the full bot response
        
        # Simulate line-by-line generation
        generated_response = ""
        for word in bot_reply.split():
            generated_response += word + " "
            bot_response_placeholder.markdown(
                f"""
                <div class="chat bot">
                    <div class="bubble bot-bubble">{generated_response.strip()}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(0.1)  # Delay for simulating text generation

    # Finalize the bot's response
    bot_response_placeholder.empty()  # Clear placeholder
    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    render_chat()  # Re-render the chat with the final response
