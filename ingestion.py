import chromadb
from embeddings import FastEmbedWrapper
from langchain_text_splitters import RecursiveCharacterTextSplitter

def ingest_data():
    print("Reading sample.txt...")
    # 1. Read the sample text file
    with open("sample.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # 2. Chunk the text using RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30,
        length_function=len,
        is_separator_regex=False,
        separators=["\\n\\n", "\\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    
    # 3. Initialize ChromaDB persistent client
    print("Initializing ChromaDB persistent client...")
    client = chromadb.PersistentClient(path="./chroma_data")

    # 4. Use custom FastEmbed wrapper
    print("Setting up custom FastEmbed wrapper (BAAI/bge-small-en-v1.5)...")
    embedding_function = FastEmbedWrapper()

    # 5. Create or get collection
    print("Creating/getting 'rag_collection'...")
    collection = client.get_or_create_collection(
        name="rag_collection",
        embedding_function=embedding_function
    )

    # 6. Store chunks and their embeddings in ChromaDB
    print("Generating embeddings and storing in ChromaDB...")
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    
    collection.add(
        documents=chunks,
        ids=ids
    )
    
    print(f"Successfully ingested {len(chunks)} chunks into ChromaDB.")

if __name__ == "__main__":
    ingest_data()
