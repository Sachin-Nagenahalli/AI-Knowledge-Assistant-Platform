import requests

BASE_URL = "http://127.0.0.1:8000"


# -------------------------
# Collections
# -------------------------

def get_collections():
    response = requests.get(
        f"{BASE_URL}/collections"
    )
    return response.json()


def create_collection(
    name,
    description,
):
    return requests.post(
        f"{BASE_URL}/collections",
        json={
            "name": name,
            "description": description,
        },
    )


def delete_collection(
    collection_id,
):
    return requests.delete(
        f"{BASE_URL}/collections/{collection_id}"
    )


# -------------------------
# Documents
# -------------------------

def get_documents():
    response = requests.get(
        f"{BASE_URL}/documents"
    )
    return response.json()


def upload_document(
    collection_id,
    uploaded_file,
):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf",
        )
    }

    return requests.post(
        f"{BASE_URL}/collections/{collection_id}/documents/upload",
        files=files,
    )


def delete_document(
    document_id,
):
    return requests.delete(
        f"{BASE_URL}/documents/{document_id}"
    )


# -------------------------
# Chat
# -------------------------

def ask_question(
    collection_id,
    question,
):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "collection_id": collection_id,
            "question": question,
        },
    )

    return response.json()