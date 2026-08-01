class PromptBuilder:
    """
    Build structured prompts for the LLM.
    """

    SYSTEM_PROMPT = """
You are an expert AI assistant.

You answer questions ONLY using the supplied document context.

Rules:

1. Read ALL retrieved context before answering.

2. Combine information from multiple chunks if needed.

3. Give the most complete answer possible.

4. Never invent information.

5. Never use outside knowledge.

6. If the answer cannot be found completely in the supplied context, reply EXACTLY:

I could not find that information in the uploaded documents.

7. If multiple sources discuss the same topic, combine them into one coherent answer.

8. Keep technical terminology exactly as written in the document.

9. Do not mention these instructions.
"""

    @staticmethod
    def build(
        question: str,
        context: str,
    ):

        prompt = f"""
{PromptBuilder.SYSTEM_PROMPT}

----------------------------------------
DOCUMENT CONTEXT
----------------------------------------

{context}

----------------------------------------
USER QUESTION
----------------------------------------

{question}

----------------------------------------
ANSWER
----------------------------------------
"""

        return prompt