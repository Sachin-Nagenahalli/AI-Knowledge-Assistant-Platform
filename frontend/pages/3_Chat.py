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

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            with st.expander("📚 Sources"):

                for source in message["sources"]:

                    st.write(source)

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

            # -------------------------
            # DEBUG OUTPUT
            # -------------------------
            st.subheader("🐞 Debug Response")
            st.json(response)

            answer = response.get(
                "answer",
                "No answer returned."
            )

            st.markdown(answer)

            if "sources" in response:

                with st.expander("📚 Sources", expanded=True):

                    for source in response["sources"]:

                        st.json(source)

            else:

                st.warning(
                    "No sources returned by the backend."
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": response.get("sources", []),
        }
    )