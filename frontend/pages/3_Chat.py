import streamlit as st

from components.api import (
    ask_question,
    get_collections,
)

st.set_page_config(
    page_title="AI Chat",
    page_icon="💬",
    layout="wide",
)

st.title("💬 AI Knowledge Chat")

collections = get_collections()

if not collections:
    st.warning("Create a collection first.")
    st.stop()

collection_map = {
    collection["name"]: collection
    for collection in collections
}

selected_name = st.selectbox(
    "Select Collection",
    list(collection_map.keys()),
)

selected_collection = collection_map[selected_name]

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Previous Conversation
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):

            with st.expander("📚 Sources"):

                for source in message["sources"]:

                    st.markdown(
                        f"""
### 📄 {source['filename']}

- **Document ID:** {source['document_id']}
- **Chunk:** {source['chunk']}
- **Similarity:** {source['score'] * 100:.1f}%
"""
                    )

# -----------------------------
# User Input
# -----------------------------
question = st.chat_input(
    "Ask anything about your documents..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ask_question(
                selected_collection["id"],
                question,
            )

            answer = response.get(
                "answer",
                "No answer returned."
            )

            st.markdown(answer)

            sources = response.get(
                "sources",
                []
            )

            if sources:

                with st.expander(
                    "📚 Sources",
                    expanded=False,
                ):

                    for source in sources:

                        st.markdown(
                            f"""
### 📄 {source['filename']}

- **Document ID:** {source['document_id']}
- **Chunk:** {source['chunk']}
- **Similarity:** {source['score'] * 100:.1f}%
"""
                        )

            else:

                st.info(
                    "No source documents were returned."
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
        }
    )