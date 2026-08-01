from dataclasses import dataclass, field


@dataclass
class Chunk:

    id: str

    text: str

    metadata: dict

    score: float = 0.0


@dataclass
class RetrievalResult:

    query: str

    chunks: list[Chunk] = field(
        default_factory=list
    )


@dataclass
class Source:

    filename: str

    document_id: int

    collection_id: int

    chunk: int

    score: float


@dataclass
class AnswerResult:

    answer: str

    sources: list[Source] = field(
        default_factory=list
    )

    confidence: float = 0.0