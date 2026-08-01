import streamlit as st

from components.api import (
    create_collection,
    delete_collection,
    get_collections,
)

st.set_page_config(
    page_title="Collections",
    page_icon="📂",
    layout="wide",
)

st.title("📂 Collections")

st.divider()

with st.expander("➕ Create Collection"):

    with st.form("create_collection"):

        name = st.text_input("Name")

        description = st.text_area("Description")

        submitted = st.form_submit_button(
            "Create"
        )

        if submitted:

            response = create_collection(
                name,
                description,
            )

            if response.status_code == 200:
                st.success("Created")
                st.rerun()

            elif response.status_code == 409:
                st.warning("Already exists")

            else:
                st.error(response.text)

st.divider()

collections = get_collections()

st.subheader(
    f"Collections ({len(collections)})"
)

for collection in collections:

    with st.container(border=True):

        col1, col2 = st.columns([6, 1])

        with col1:

            st.markdown(
                f"### 📁 {collection['name']}"
            )

            st.write(
                collection["description"]
            )

            st.caption(
                f"ID : {collection['id']}"
            )

        with col2:

            if st.button(
                "🗑",
                key=collection["id"],
            ):

                delete_collection(
                    collection["id"]
                )

                st.rerun()