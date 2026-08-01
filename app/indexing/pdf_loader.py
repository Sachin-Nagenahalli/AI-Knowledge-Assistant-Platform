from pathlib import Path

from pypdf import PdfReader

from app.core.logger import logger


def extract_text(
    pdf_path: str,
) -> str:
    """
    Extract text from a PDF document.
    """

    pdf_file = Path(pdf_path)

    if not pdf_file.exists():

        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    try:

        reader = PdfReader(pdf_file)

    except Exception as e:

        logger.exception(
            f"Unable to open PDF: {e}"
        )

        raise RuntimeError(
            f"Unable to open PDF: {e}"
        )

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1,
    ):

        try:

            text = page.extract_text()

            if text:

                pages.append(
                    text.strip()
                )

        except Exception as e:

            logger.warning(
                f"Skipping page {page_number}: {e}"
            )

    document_text = "\n\n".join(
        pages
    )

    if not document_text.strip():

        raise RuntimeError(
            "No readable text found in the PDF."
        )

    return document_text