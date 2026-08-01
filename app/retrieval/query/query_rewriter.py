class QueryRewriter:

    def rewrite(
        self,
        question: str,
    ) -> list[str]:
        """
        Generate retrieval queries.

        Version 1:
        Return the original question.

        Future versions:
        - Multi-query
        - HyDE
        - Step-back prompting
        """

        return [question]