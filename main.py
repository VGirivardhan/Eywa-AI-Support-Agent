import streamlit as st
from chat_handler import get_bot_response

# Page Configuration
st.set_page_config(page_title="Eywa - AI Support Agent", layout="centered", initial_sidebar_state="collapsed")

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Company Logo
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <img src="company_logo.png" alt="Company Logo" style="width: 200px;" />
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
    # Add user's message to the chat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get the bot's response
    with st.spinner("Eywa is typing..."):
        bot_reply = get_bot_response(user_input)
    
    # Add bot's response to the chat
    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    
    # Re-render the app to show updated chat messages
    st.rerun()
