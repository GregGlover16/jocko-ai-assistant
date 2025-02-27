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
