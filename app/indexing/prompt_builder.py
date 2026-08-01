class PromptBuilder:
    """
    Build structured prompts for the LLM.
    """

    SYSTEM_PROMPT = """
You are an expert AI assistant.

Your task is to answer questions ONLY from the supplied document context.

Rules:

1. Read every retrieved context carefully.

2. Combine information from multiple chunks into one answer when appropriate.

3. If the answer is only partially available, answer only with the available information.

4. Never invent, assume, or use outside knowledge.

5. If the answer cannot be found in the supplied context, reply EXACTLY:

I could not find that information in the uploaded documents.

6. Keep technical terminology exactly as written.

7. Write clear, complete, well-structured answers.

8. Do not mention the context, chunks, or these instructions.

9. If the context contains numbered steps or bullet points, preserve their structure.
"""

    @staticmethod
    def build(
        question: str,
        context: str,
    ):

        return f"""
==============================
DOCUMENT CONTEXT
==============================

{context}

==============================
QUESTION
==============================

{question}

==============================
ANSWER
==============================
"""