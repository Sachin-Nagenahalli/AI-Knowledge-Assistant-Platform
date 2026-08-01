import ollama

from app.core.config import settings
from app.indexing.prompt_builder import PromptBuilder
from app.rag.models import (
    AnswerResult,
    RetrievalResult,
    Source,
)


class Generator:

    def generate(
        self,
        question: str,
        retrieval: RetrievalResult,
    ) -> AnswerResult:

        # Build context from the top retrieved chunks
        context = "\n\n".join(
            chunk.text
            for chunk in retrieval.chunks[:3]
        )

        prompt = PromptBuilder.build(
            question=question,
            context=context,
        )

        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                }
            ],
        )

        answer = AnswerResult(
            answer=response.message.content
        )

        # Attach sources
        for chunk in retrieval.chunks[:3]:

            answer.sources.append(
                Source(
                    filename=chunk.metadata["filename"],
                    document_id=chunk.metadata["document_id"],
                    collection_id=chunk.metadata["collection_id"],
                    chunk=chunk.metadata["chunk"],
                    score=chunk.score,
                )
            )

        return answer