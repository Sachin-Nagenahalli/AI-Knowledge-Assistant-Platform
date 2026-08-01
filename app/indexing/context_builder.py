class ContextBuilder:
    """
    Build the final context passed to the LLM.
    """

    @staticmethod
    def build(
        results,
        top_n: int = 3,
    ):

        documents = results["documents"][0]

        metadatas = results["metadatas"][0]

        context_parts = []

        for document, metadata in zip(
            documents[:top_n],
            metadatas[:top_n],
        ):

            context_parts.append(
                f"""
========================================
DOCUMENT
========================================

Filename:
{metadata.get("filename")}

Document ID:
{metadata.get("document_id")}

Chunk:
{metadata.get("chunk")}

----------------------------------------

{document}
"""
            )

        return "\n".join(
            context_parts
        )