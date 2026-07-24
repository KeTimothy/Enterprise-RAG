from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
import logging


@dataclass(frozen=True)
class EmbeddingServiceConfig:
    """
    Configuration for the EmbeddingService.
    """

    model_name: str = "BAAI/bge-small-en-v1.5"
    query_instruction: str | None = None
    normalize_embeddings: bool = True

class SupportedModels:
    """
    A class to hold supported model names as constants.
    """

    BGE_SMALL_EN_V1_5 = EmbeddingServiceConfig(
        model_name="BAAI/bge-small-en-v1.5",
        query_instruction="Represent this sentence for searching relevant passages: "
    )


class EmbeddingService:
    """
    Service responsible for generating vector embeddings from text.

    This class wraps the SentenceTransformer model so that the rest of
    the application does not depend on a specific embedding provider.
    """

    def __init__(
            self,
            config: EmbeddingServiceConfig = SupportedModels.BGE_SMALL_EN_V1_5) -> None:
        """
        Initialize the embedding model.

        Args:
            config (EmbeddingServiceConfig): Configuration for the embedding service.
        """
        logging.info(
            "Creating EmbeddingService with model: %s",
            config.model_name,
        )
        self.config = config
        self._model: SentenceTransformer | None = None

    @property
    def model(self) -> SentenceTransformer:
        """
        Lazy-load the embedding model.

        Returns:
            SentenceTransformer: The loaded embedding model.
        """
        if self._model is None:
            logging.info("Loading embedding model: %s", self.config.model_name)
            self._model = SentenceTransformer(self.config.model_name)
        return self._model
    
    def embed_text(self, text: str) -> list[float]:
        """
        Generate an embedding for a single piece of text.

        Args:
            text: Input text.

        Returns:
            Embedding vector as a list of floats.
        """
        return self.embed_batch([text])[0]

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
            normalize_embeddings=self.config.normalize_embeddings,
        )
        return embeddings.tolist()

    def embed_query(self, query: str) -> list[float]:
        """
        Dynamically generate an embedding for a query, optionally using instructions.
        
        Args:
            query: Input query string.
        Returns:
            Embedding vector as a list of floats.
        """
        if self.config.query_instruction:
            query = f"{self.config.query_instruction}{query}"
        
        return self.embed_batch([query])[0]


