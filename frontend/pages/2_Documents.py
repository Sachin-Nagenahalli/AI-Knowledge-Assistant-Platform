import streamlit as st

from components.api import (
    get_collections,
    get_documents,
    upload_document,
)

st.set_page_config(
    page_title="Documents",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Document Management")

st.markdown(
    "Upload PDFs into your collections."
)

st.divider()

collections = get_collections()

if not collections:

    st.warning(
        "Create a collection first."
    )

    st.stop()

collection_names = [
    collection["name"]
    for collection in collections
]

selected_name = st.selectbox(
    "Select Collection",
    collection_names,
)

selected_collection = next(
    collection
    for collection in collections
    if collection["name"] == selected_name
)

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"],
)

if st.button("Upload Document"):

    if uploaded_file is None:

        st.warning(
            "Please choose a PDF."
        )

    else:

        response = upload_document(
            selected_collection["id"],
            uploaded_file,
        )

        if response.status_code == 200:

            st.success(
                "Document uploaded successfully."
            )

        elif response.status_code == 409:

            st.warning(
                "Document already exists."
            )

        else:

            st.error(
                response.text
            )

st.divider()

st.subheader("Indexed Documents")

documents = get_documents()

if not documents:

    st.info(
        "No documents uploaded."
    )

else:

    for document in documents:

        with st.container(border=True):

            st.markdown(
                f"### 📄 {document['filename']}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"Status : {document['status']}"
                )

            with col2:
                st.write(
                    f"Collection ID : {document['collection_id']}"
                )