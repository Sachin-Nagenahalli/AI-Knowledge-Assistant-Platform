import re

MIN_WORDS = 200
MAX_WORDS = 450
OVERLAP_WORDS = 75


def normalize_text(text: str):
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

    return [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]


def word_count(text: str):

    return len(text.split())


def overlap_text(chunk: str):
    """
    Return the last OVERLAP_WORDS words from a chunk.
    """

    words = chunk.split()

    if len(words) <= OVERLAP_WORDS:
        return chunk

    return " ".join(
        words[-OVERLAP_WORDS:]
    )


def semantic_chunk(text: str):
    """
    Paragraph-based semantic chunking with overlap.
    """

    text = normalize_text(text)

    if not text:
        return []

    paragraphs = split_paragraphs(text)

    chunks = []

    current_chunk = []

    current_words = 0

    for paragraph in paragraphs:

        words = word_count(paragraph)

        # Skip empty paragraphs
        if words == 0:
            continue

        # Paragraph fits inside current chunk
        if current_words + words <= MAX_WORDS:

            current_chunk.append(paragraph)

            current_words += words

        else:

            # Save current chunk only if it has content
            if current_chunk:

                chunk = "\n\n".join(current_chunk).strip()

                if chunk:
                    chunks.append(chunk)

                overlap = overlap_text(chunk)

                current_chunk = []

                if overlap:
                    current_chunk.append(overlap)

                current_chunk.append(paragraph)

                current_words = (
                    word_count(overlap)
                    + words
                )

            else:
                # Handle very large paragraph
                chunks.append(paragraph.strip())

                current_chunk = []

                current_words = 0

    # Save remaining chunk
    if current_chunk:

        chunk = "\n\n".join(current_chunk).strip()

        if chunk:
            chunks.append(chunk)

    # Final cleanup
    chunks = [
        chunk
        for chunk in chunks
        if chunk.strip()
    ]

    return chunks