from pathlib import Path

from pypdf import PdfReader


class IngestionService:
    """
    Service responsible for reading and processing PDF documents.
    """

    def extract_text(self, pdf_path: str | Path) -> str:
        """
        Extract all text from a PDF.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Combined text from every page.
        """

        reader = PdfReader(pdf_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    def chunk_text(self, text: str, chunk_size: int = 500, chunk_overlap: int = 100) -> list[str]:
        """
        Split text into overlapping chunks.

        Args:
            text: Input text.
            chunk_size: Maximum number of characters per chunk.
            chunk_overlap: Number of overlapping characters between chunks.

        Returns:
            List of text chunks.
        """
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = text[start:end]
            chunks.append(chunk)
            start += chunk_size - chunk_overlap

        return chunks

        
ingestion_service = IngestionService()