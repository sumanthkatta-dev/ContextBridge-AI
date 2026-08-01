import chromadb
from embeddings import FastEmbedWrapper
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("RAG Server")

# Initialize ChromaDB client and collection globally
client = chromadb.PersistentClient(path="./chroma_data")
embedding_function = FastEmbedWrapper()
collection = client.get_or_create_collection(
    name="rag_collection",
    embedding_function=embedding_function
)

@mcp.tool()
def retrieve_documents(query: str, n_results: int = 3) -> str:
    """
    Search the ChromaDB vector database for the given query and return the most relevant text chunks.
    
    Args:
        query: The search query string.
        n_results: The number of results to return.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    if not results or not results['documents'] or not results['documents'][0]:
        return "No results found."
    
    retrieved_texts = results['documents'][0]
    response = f"Retrieved {len(retrieved_texts)} chunks for query: '{query}'\n\n"
    
    for i, text in enumerate(retrieved_texts, 1):
        response += f"--- Chunk {i} ---\n{text}\n\n"
        
    return response

if __name__ == "__main__":
    # Start the FastMCP server with SSE transport on port 8000
    print("Starting FastMCP RAG Server with SSE on port 8000...")
    # NOTE: In FastMCP, transport="sse" typically defaults to port 8000.
    # To explicitly set the port, use environmental variables or passing it if the API supports it.
    try:
        mcp.run(transport="sse", port=8000)
    except TypeError:
        # Fallback if port isn't supported as an argument
        mcp.run(transport="sse")
