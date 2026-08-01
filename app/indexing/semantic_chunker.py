import re


MIN_WORDS = 200
MAX_WORDS = 450


def normalize_text(text: str) -> str:
    """
    Clean extracted PDF text.
    """

    text = text.replace("\r", "\n")

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    return text.strip()


def split_paragraphs(text: str):
    """
    Split text into paragraphs.
    """

    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    return paragraphs


def word_count(text: str):
    return len(text.split())


def semantic_chunk(text: str):
    """
    Create paragraph-based semantic chunks.
    """

    text = normalize_text(text)

    paragraphs = split_paragraphs(text)

    chunks = []

    current_chunk = []

    current_words = 0

    for paragraph in paragraphs:

        words = word_count(paragraph)

        if (
            current_words + words
            <= MAX_WORDS
        ):

            current_chunk.append(
                paragraph
            )

            current_words += words

        else:

            if current_chunk:

                chunks.append(
                    "\n\n".join(
                        current_chunk
                    )
                )

            current_chunk = [
                paragraph
            ]

            current_words = words

    if current_chunk:

        chunks.append(
            "\n\n".join(
                current_chunk
            )
        )

    return chunks