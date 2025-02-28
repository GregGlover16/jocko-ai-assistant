import os
import json
from openai import OpenAI
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# Debug: Print environment variables
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))
print("Pinecone API Key:", os.getenv("PINECONE_API_KEY"))
print("Pinecone Environment:", os.getenv("PINECONE_ENVIRONMENT"))

# Initialize OpenAI and Pinecone
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Load JSON files
def load_json_files(data_dir):
    data = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                data.extend(json.load(f))
    return data

# Extract text based on the type of data
def extract_text(item):
    if "content" in item:  # For YouTube transcripts
        return item["content"]
    elif "quote" in item:  # For quotes
        return item["quote"]
    elif "book_title" in item:  # For books
        return f"{item['book_title']} - {item['chapter_title']}: {item['content']}"
    else:
        raise KeyError(f"Unknown data format: {item}")

# Generate embeddings
def generate_embeddings(texts):
    embeddings = []
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=8000,  # Maximum number of tokens per chunk
        chunk_overlap=200,  # Overlap between chunks to preserve context
        length_function=len,  # Function to measure chunk length
    )

    for text in texts:
        chunks = text_splitter.split_text(text)
        for chunk in chunks:
            response = client.embeddings.create(input=chunk, model="text-embedding-ada-002")
            embeddings.extend([item.embedding for item in response.data])
    return embeddings

# Store embeddings in Pinecone
def store_embeddings(index_name, texts, embeddings):
    index = pc.Index(index_name)
    vectors = [(str(i), embedding) for i, embedding in enumerate(embeddings)]
    index.upsert(vectors)

# Main function
def main():
    data_dir = "data"
    index_name = "jocko-ai-assistant"

    # Load data
    print("Loading JSON files...")
    data = load_json_files(data_dir)
    print(f"Loaded {len(data)} items.")  # Debug: Print number of items loaded

    # Extract text from data
    texts = [extract_text(item) for item in data]

    # Generate embeddings
    print("Generating embeddings...")
    embeddings = generate_embeddings(texts)
    print(f"Generated {len(embeddings)} embeddings.")  # Debug: Print number of embeddings

    # Store embeddings in Pinecone
    print("Storing embeddings in Pinecone...")
    store_embeddings(index_name, texts, embeddings)
    print("Embeddings stored successfully!")

if __name__ == "__main__":
    main()