from app.rag.models import (
    AnswerResult,
    RetrievalResult,
)


class Validator:

    def validate(
        self,
        answer: AnswerResult,
        retrieval: RetrievalResult,
    ) -> AnswerResult:
        """
        Version 1

        Future versions will:

        - Detect hallucinations
        - Verify sources
        - Compute confidence
        - Trigger re-retrieval
        """

        if len(retrieval.chunks) > 0:

            answer.confidence = round(

                sum(
                    chunk.score
                    for chunk in retrieval.chunks[:3]
                )
                /
                min(
                    len(retrieval.chunks),
                    3,
                ),

                3,

            )

        else:

            answer.confidence = 0.0

        return answer