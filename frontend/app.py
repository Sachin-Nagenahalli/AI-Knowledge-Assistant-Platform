import streamlit as st

from components.sidebar import show_sidebar


st.set_page_config(
    page_title="AI Knowledge Platform",
    page_icon="🤖",
    layout="wide",
)

show_sidebar()

st.title("🤖 AI Knowledge Platform")

st.markdown(
    """
Welcome to your Local RAG System.

Use the pages on the left to:

- 📂 Manage Collections
- 📄 Upload Documents
- 💬 Chat with your Documents
"""
)

st.success("Frontend is running successfully!")