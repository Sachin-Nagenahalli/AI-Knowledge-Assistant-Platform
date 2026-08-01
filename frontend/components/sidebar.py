import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🤖 AI Knowledge Platform")

        st.markdown("---")

        st.success("🟢 Backend Connected")

        st.markdown("---")

        st.subheader("Project")

        st.write("Local RAG System")

        st.markdown("---")

        st.subheader("Technology")

        st.write("⚡ FastAPI")
        st.write("🧠 Ollama")
        st.write("📚 ChromaDB")
        st.write("🗄 SQLite")
        st.write("🎨 Streamlit")

        st.markdown("---")

        st.caption("Version 1.0")