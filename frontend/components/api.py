import streamlit as st

from components.sidebar import show_sidebar
from components.styles import load_css
from components.api import (
    get_collections,
    get_documents,
)

st.set_page_config(
    page_title="AI Knowledge Platform",
    page_icon="🤖",
    layout="wide",
)

load_css()

show_sidebar()

st.title("🤖 AI Knowledge Platform")

st.caption(
    "A Local Retrieval-Augmented Generation (RAG) System"
)

collections = get_collections()
documents = get_documents()

st.markdown("## 📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Collections",
        len(collections),
    )

with col2:
    st.metric(
        "Documents",
        len(documents),
    )

with col3:
    st.metric(
        "Backend",
        "🟢 Online",
    )

st.divider()

left, right = st.columns(2)

with left:

    st.subheader("📂 Collections")

    if collections:

        for collection in collections:

            with st.container(border=True):

                st.markdown(
                    f"### 📁 {collection['name']}"
                )

                st.write(
                    collection["description"]
                )

    else:

        st.info(
            "No collections available."
        )

with right:

    st.subheader("📄 Documents")

    if documents:

        for document in documents:

            with st.container(border=True):

                st.markdown(
                    f"### 📄 {document['filename']}"
                )

                st.write(
                    f"Status : {document['status']}"
                )

    else:

        st.info(
            "No documents uploaded."
        )

st.divider()

st.subheader("⚙️ Models")

col1, col2 = st.columns(2)

with col1:

    st.info("Embedding Model")

    st.code(
        "embeddinggemma"
    )

with col2:

    st.info("LLM")

    st.code(
        "qwen2.5:3b"
    )