from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
from openai import OpenAI
from pinecone import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI and Pinecone
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Initialize FastAPI
app = FastAPI()

# Pydantic models for request bodies
class ChatRequest(BaseModel):
    message: str

class QuizRequest(BaseModel):
    user_id: str
    question_id: str
    answer: str

# In-memory storage for quizzes (replace with MongoDB later)
quizzes = {
    "q1": {
        "question": "What is the core principle of Extreme Ownership?",
        "options": ["Blame others", "Take full responsibility", "Avoid decisions"],
        "correct_answer": "Take full responsibility"
    }
}

# Endpoint: Chat with Jocko
@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint to chat with the Jocko AI assistant.
    """
    # Generate a response using OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Use GPT-4 for better responses
            messages=[
                {"role": "system", "content": "You are Jocko Willink, a retired Navy SEAL and leadership expert. Respond in Jocko's voice and tone."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=150,  # Limit the response length
            temperature=0.7  # Control creativity (0 = strict, 1 = creative)
        )
        jocko_response = response.choices[0].message.content
        return {"response": jocko_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Get a book summary
@app.get("/summary/{book_id}/{chapter_id}")
async def get_summary(book_id: str, chapter_id: str):
    """
    Endpoint to retrieve a summary of a specific chapter from Jocko's books.
    """
    try:
        # Query Pinecone for the summary
        index = pc.Index("jocko-ai-assistant")
        query_vector = ...  # Generate or retrieve the query vector (e.g., using OpenAI embeddings)
        response = index.query(vector=query_vector, top_k=1, include_metadata=True)

        if not response.matches:
            raise HTTPException(status_code=404, detail="Summary not found")

        summary = response.matches[0].metadata.get("summary", "No summary available")
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Get a quiz question
@app.get("/quiz/{question_id}")
async def get_quiz(question_id: str):
    """
    Endpoint to retrieve a quiz question.
    """
    if question_id not in quizzes:
        raise HTTPException(status_code=404, detail="Question not found")
    return quizzes[question_id]

# Endpoint: Submit a quiz answer
@app.post("/quiz/submit")
async def submit_quiz(request: QuizRequest):
    """
    Endpoint to submit a quiz answer and track user progress.
    """
    if request.question_id not in quizzes:
        raise HTTPException(status_code=404, detail="Question not found")
    
    correct = quizzes[request.question_id]["correct_answer"] == request.answer
    return {
        "user_id": request.user_id,
        "question_id": request.question_id,
        "correct": correct
    }

# Endpoint: Get a daily quote
@app.get("/quote")
async def get_quote():
    """
    Endpoint to retrieve a daily Jocko quote.
    """
    # TODO: Retrieve a daily quote from Pinecone or another data source
    quote = "Discipline equals freedom."
    return {"quote": quote}