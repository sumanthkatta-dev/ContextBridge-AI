from chromadb import Documents, EmbeddingFunction, Embeddings
from fastembed import TextEmbedding

class FastEmbedWrapper(EmbeddingFunction):
    def __init__(self):
        self.model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        
    def __call__(self, input: Documents) -> Embeddings:
        embeddings = self.model.embed(input)
        return [e.tolist() for e in embeddings]
