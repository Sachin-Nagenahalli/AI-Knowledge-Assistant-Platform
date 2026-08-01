from app.rag.generator import Generator
from app.rag.pipeline import Pipeline
from app.rag.retriever import Retriever
from app.rag.validator import Validator


class RAGEngine:

    def __init__(self):

        self.retriever = Retriever()
        self.pipeline = Pipeline()
        self.generator = Generator()
        self.validator = Validator()

    def ask(
        self,
        collection_id: int,
        question: str,
    ):

        # Step 1: Retrieve relevant chunks
        retrieval = self.retriever.retrieve(
            query=question,
            collection_id=collection_id,
        )

        # Step 2: Expand context (currently placeholder)
        retrieval = self.pipeline.process(
            retrieval
        )

        # Step 3: Generate answer
        answer = self.generator.generate(
            question=question,
            retrieval=retrieval,
        )

        # Step 4: Validate answer
        answer = self.validator.validate(
            answer=answer,
            retrieval=retrieval,
        )

        return answer