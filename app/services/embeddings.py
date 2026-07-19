from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Service responsible for generating vector embeddings from text.

    This class wraps the SentenceTransformer model so that the rest of
    the application does not depend on a specific embedding provider.
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5") -> None:
        """
        Initialize the embedding model.

        Args:
            model_name: Hugging Face model identifier.
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> list[float]:
        """
        Generate an embedding for a single piece of text.

        Args:
            text: Input text.

        Returns:
            Embedding vector as a list of floats.
        """
        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )
        return embedding.tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of input texts.

        Returns:
            List of embedding vectors.
        """
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )
        return embeddings.tolist()


embedding_service = EmbeddingService()