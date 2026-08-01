import streamlit as st

from components.api import (
    get_collections,
    get_documents,
    upload_document,
    delete_document,
)

st.set_page_config(
    page_title="Documents",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Document Management")

st.write("Upload and manage your documents.")

st.divider()

collections = get_collections()

if not collections:
    st.warning("Create a collection first.")
    st.stop()

collection_names = [
    collection["name"]
    for collection in collections
]

selected_name = st.selectbox(
    "Collection",
    collection_names,
)

selected_collection = next(
    collection
    for collection in collections
    if collection["name"] == selected_name
)

uploaded_file = st.file_uploader(
    "Choose PDF",
    type=["pdf"],
)

if st.button("Upload"):

    if uploaded_file is None:

        st.warning("Choose a PDF.")

    else:

        response = upload_document(
            selected_collection["id"],
            uploaded_file,
        )

        if response.status_code == 200:

            st.success("Document uploaded.")

            st.rerun()

        elif response.status_code == 409:

            st.warning("Document already exists.")

        else:

            st.error(response.text)

st.divider()

st.subheader("Documents")

documents = get_documents()

if not documents:

    st.info("No documents uploaded.")

else:

    for document in documents:

        with st.container(border=True):

            col1, col2 = st.columns([8,1])

            with col1:

                st.markdown(
                    f"### 📄 {document['filename']}"
                )

                st.write(
                    f"Status : **{document['status']}**"
                )

                st.write(
                    f"Collection : **{document['collection_id']}**"
                )

                st.caption(
                    f"Document ID : {document['id']}"
                )

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{document['id']}",
                ):

                    response = delete_document(
                        document["id"]
                    )

                    if response.status_code == 200:

                        st.success(
                            "Deleted successfully."
                        )

                        st.rerun()

                    else:

                        st.error(
                            response.text
                        )