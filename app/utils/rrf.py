from collections import defaultdict


class ReciprocalRankFusion:

    def __init__(self, k: int = 60):
        self.k = k

    def fuse(self, vector_results, bm25_results):

        scores = defaultdict(float)

        # Vector ranking
        vector_ids = vector_results["ids"][0]

        for rank, chunk_id in enumerate(vector_ids):
            scores[chunk_id] += 1 / (self.k + rank + 1)

        # BM25 ranking
        for rank, item in enumerate(bm25_results):
            chunk_id = item[0]
            scores[chunk_id] += 1 / (self.k + rank + 1)

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranked