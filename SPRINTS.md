# Jocko AI Assistant - Sprint Documentation

## Sprint 0 - Create Sprint Documentation
**Goal**: Create a `SPRINTS.md` file to document all sprint instructions and progress.

### Steps
1. Created the `SPRINTS.md` file using the `echo` command.
2. Added a header and initial content for Sprint 0.
3. Pushed the file to GitHub.

### Notes
- This file will be updated after each sprint to include new instructions and progress.


## Sprint 1 - Project Setup & GitHub Repository
**Goal**: Set up the GitHub repository and organize files for future development.

### Steps
1. Created a GitHub repository named `jocko-ai-assistant`.
2. Cloned the repository locally.
3. Organized the folder structure:
   - `data/`: Contains JSON files for Jocko's books, transcripts, and quotes.
   - `backend/`: Future FastAPI code.
   - `frontend/`: Future Streamlit/Next.js code.
   - `scripts/`: Utility scripts for embeddings and other tasks.
4. Added placeholder files (`.gitkeep`) to track empty folders.
5. Created a `.gitignore` file to exclude unnecessary files.

### Notes
- Used `echo` to create `.gitignore` on Windows.
- Added `.gitkeep` files to ensure empty folders are tracked by Git.


## Sprint 2 - Set Up the Python Environment
**Goal**: Set up a Python virtual environment and install required dependencies.

### Steps
1. Created a Python virtual environment using `python -m venv venv`.
2. Installed dependencies (`openai`, `pinecone-client`, `langchain`, etc.) using `pip install -r requirements.txt`.
3. Verified the structure of JSON files in the `data/` folder.


## Sprint 3 - Generate Embeddings for JSON Files
**Goal**: Use OpenAI to generate embeddings for Jocko’s books, quotes, and YouTube transcripts, and store them in Pinecone.

### Steps
1. Set up OpenAI and Pinecone API keys in `.env`.
2. Created a script (`scripts/generate_embeddings.py`) to:
   - Load JSON files from the `data/` folder.
   - Extract text using a custom `extract_text` function.
   - Split text into chunks using LangChain’s `RecursiveCharacterTextSplitter`.
   - Generate embeddings using OpenAI’s `text-embedding-ada-002` model.
   - Store embeddings in Pinecone.
3. Tested the script to ensure it handles large inputs and different JSON formats.
4. Updated the GitHub repository with the completed work.

### Files Added/Modified
- `scripts/generate_embeddings.py`
- `.env`
- `requirements.txt`
- `SPRINTS.md`


## Sprint 4 - FastAPI Setup and Base Code
**Goal**: Set up a FastAPI backend with basic endpoints.

### Steps
1. Created a `setup_main.py` file in the `backend` folder with the following endpoints:
   - `/chat`: Chat with the Jocko AI assistant.
   - `/summary/{book_id}/{chapter_id}`: Retrieve a book summary.
   - `/quiz/{question_id}`: Retrieve a quiz question.
   - `/quiz/submit`: Submit a quiz answer.
   - `/quote`: Retrieve a daily Jocko quote.
2. Run the FastAPI App
   -  Run the FastAPI app using Uvicorn:

uvicorn main:app --reload

   -  Open your browser and go to:
http://127.0.0.1:8000/ to see the welcome message.
http://127.0.0.1:8000/docs to access the interactive API documentation (Swagger UI).

3. Tested the endpoints using FastAPI’s interactive documentation.
   -  Chat with Jocko:
Go to the /chat endpoint in Swagger UI.
Enter a message (e.g., {"message": "How can I be more disciplined?"}).
Submit the request and check the response.
   -  Get a Book Summary:
Go to the /summary/{book_id}/{chapter_id} endpoint.
Enter a book_id and chapter_id (e.g., book_id=book1, chapter_id=chapter1).
Submit the request and check the response.
   -  Get a Quiz Question:
Go to the /quiz/{question_id} endpoint.
Enter a question_id (e.g., q1).
Submit the request and check the response.
   -  Submit a Quiz Answer:
Go to the /quiz/submit endpoint.
Enter a user_id, question_id, and answer (e.g., {"user_id": "user1", "question_id": "q1", "answer": "Take full responsibility"}).
Submit the request and check the response.
   -  Get a Daily Quote:
Go to the /quote endpoint.
Submit the request and check the response.

### Files Added/Modified
- `backend/setu_main.py`
- `requirements.txt`
- `SPRINTS.md`