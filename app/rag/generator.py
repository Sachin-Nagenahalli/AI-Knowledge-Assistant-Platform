import ollama

from app.core.config import settings
from app.indexing.prompt_builder import PromptBuilder
from app.rag.models import (
    AnswerResult,
    RetrievalResult,
    Source,
)


client = ollama.Client(
    host=settings.OLLAMA_URL
)


class Generator:

    def generate(
        self,
        question: str,
        retrieval: RetrievalResult,
    ) -> AnswerResult:

        # ----------------------------
        # No Context Found
        # ----------------------------

        if not retrieval.chunks:

            answer = AnswerResult(
                answer="I could not find that information in the uploaded documents."
            )

            answer.confidence = 0

            return answer

        # ----------------------------
        # Build Context
        # ----------------------------

        seen = set()

        context_chunks = []

        for chunk in retrieval.chunks:

            if chunk.id in seen:
                continue

            seen.add(chunk.id)

            context_chunks.append(
                chunk.text
            )

            if len(context_chunks) == 5:
                break

        context = "\n\n".join(
            context_chunks
        )

        # ----------------------------
        # Build Prompt
        # ----------------------------

        prompt = PromptBuilder.build(
            question=question,
            context=context,
        )

        # ----------------------------
        # Generate Answer
        # ----------------------------

        try:

            response = client.chat(
                model=settings.LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    }
                ],
            )

        except Exception as e:

            raise RuntimeError(
                f"Ollama generation failed: {e}"
            )

        answer = AnswerResult(
            answer=response.message.content
        )

        # ----------------------------
        # Attach Sources
        # ----------------------------

        seen_sources = set()

        for chunk in retrieval.chunks:

            key = (
                chunk.metadata["document_id"],
                chunk.metadata["chunk"],
            )

            if key in seen_sources:
                continue

            seen_sources.add(key)

            answer.sources.append(

                Source(

                    filename=chunk.metadata["filename"],

                    document_id=chunk.metadata["document_id"],

                    collection_id=chunk.metadata["collection_id"],

                    chunk=chunk.metadata["chunk"],

                    score=chunk.score,

                )

            )

            if len(answer.sources) == 5:
                break

        if answer.sources:

            answer.confidence = round(
                sum(source.score for source in answer.sources)
                / len(answer.sources),
                3,
            )

        else:

            answer.confidence = 0

        return answer