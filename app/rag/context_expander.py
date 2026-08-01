from app.rag.chunk_repository import ChunkRepository


class ContextExpander:

    def __init__(self):

        self.repo = ChunkRepository()

    def expand(
        self,
        retrieval,
    ):

        expanded = []

        visited = set()

        for chunk in retrieval.chunks:

            current = chunk.metadata["chunk"]

            document = chunk.metadata["document_id"]

            for neighbour in [
                current - 1,
                current,
                current + 1,
            ]:

                key = (
                    document,
                    neighbour,
                )

                if key in visited:
                    continue

                visited.add(key)

                result = self.repo.get_chunk(
                    document,
                    neighbour,
                )

                if result:

                    expanded.append(
                        result
                    )

        return expanded