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

# ---------------------------------
# Create Collection
# ---------------------------------

with st.expander("➕ Create Collection"):

    with st.form("create_collection"):

        name = st.text_input("Name")

        description = st.text_area("Description")

        submitted = st.form_submit_button(
            "Create"
        )

        if submitted:

            name = name.strip()
            description = description.strip()

            if not name:

                st.error(
                    "Collection name cannot be empty."
                )

            else:

                response = create_collection(
                    name,
                    description,
                )

                if response.status_code == 200:

                    st.success(
                        "Collection created successfully."
                    )

                    st.rerun()

                elif response.status_code == 409:

                    st.warning(
                        "Collection already exists."
                    )

                else:

                    st.error(
                        response.text
                    )

st.divider()

# ---------------------------------
# Collection List
# ---------------------------------

collections = get_collections()

st.subheader(
    f"Collections ({len(collections)})"
)

if not collections:

    st.info(
        "No collections available."
    )

else:

    for collection in collections:

        with st.container(border=True):

            col1, col2 = st.columns([6, 1])

            with col1:

                st.markdown(
                    f"### 📁 {collection['name']}"
                )

                description = collection.get(
                    "description",
                    ""
                )

                if description:

                    st.write(
                        description
                    )

                else:

                    st.caption(
                        "No description."
                    )

                st.caption(
                    f"ID : {collection['id']}"
                )

            with col2:

                if st.button(
                    "🗑",
                    key=collection["id"],
                ):

                    response = delete_collection(
                        collection["id"]
                    )

                    if response.status_code == 200:

                        st.success(
                            "Collection deleted successfully."
                        )

                        st.rerun()

                    else:

                        st.error(
                            response.text
                        )