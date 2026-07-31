from app.core.chroma import get_collection

collection = get_collection("documents")

print("Collection:", collection.name)
print("Chunks:", collection.count())