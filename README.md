# Jocko AI Assistant
A Jocko Willink-inspired AI assistant for leadership, discipline, and self-improvement.

## Folder Structure
- `data/`: Contains JSON files for Jocko's books, transcripts, and quotes.
- `backend/`: FastAPI code for the backend.
- `frontend/`: Streamlit/Next.js code for the frontend.
- `scripts/`: Utility scripts for embeddings and other tasks.

## Project Overview
This project aims to build a conversational AI assistant that mimics Jocko Willink's tone and knowledge. Features include:
- Context-aware chat responses in Jocko’s voice and tone.
- Chapter summaries and interactive quizzes from Jocko's books.
- Daily motivational quotes.
- A scoring system to track user progress.

## Tools and Technologies
- **Bubble**: No-code platform for app building.
- **MongoDB Atlas**: Database for content storage.
- **OpenAI API**: For generating AI responses.
- **Dataworkz**: For automation and workflows.

## Goals
- Learn AI tools and techniques.
- Showcase capabilities to create AI-powered applications.
- Build a prototype for future expansion into self-improvement applications.

## File Preparation and Formatting
Before running the format_book_txt_to_json.py script, .txt files must be manually preformatted to follow a structured format for processing. This step is necessary because raw text files (e.g., from transcription tools like Whisper) often lack clear markers for chapters or parts.

Required Structure for Preformatted .txt Files
Part Titles:
Each part should start with the format:
Part X - Title

Chapter Headings:
Each chapter should start with:
Chapter X. Title
Content:
Content for each chapter should follow the respective chapter heading.
Example of a Preformatted .txt File:

Part 1 - The Beginning
Chapter 1. Taking Ownership
Content for Chapter 1 goes here...

Why Manual Formatting Is Necessary
Raw text from tools like Whisper may not have clear headings or structure.
Manual formatting ensures the script can correctly parse and generate the desired JSON file.

Usage Instructions
Prepare the .txt File:
Manually structure the .txt file following the example above.

Run the the following sctripts to format the data for MongoDb ingestion:
format_book_txt_to_json.py
format_youtube_txt_json.py
format_quotes_txt_json.py

Use these scripts to convert the preformatted .txt file into a JSON file.

Verify the JSON Output:

Open the resulting JSON file and check that:
Parts and chapters are accurately represented.
Content is properly grouped under the correct chapters.

## MongoDB
Goal: Set up the database in MongoDB Atlas, including the collections necessary for your project.
Set Up MongoDB Atlas Account and Cluster:
Visit MongoDB Atlas.
Create a free account and log in.
Follow the prompts to create a Free Cluster:
Choose your cloud provider (e.g., AWS, Azure, GCP) and nearest region.
Use the default settings for other options.
Name your cluster (e.g., JockoCluster).
Click “Create Cluster.” It may take a few minutes to provision.
Create the Database and Collections:
Once the cluster is ready, go to the Database tab and click Browse Collections.
Create a new database named jocko_assistant with the following collections:
books
podcasts
quotes
users
questions
MongoDB will automatically create these collections when you insert the first document if they don’t exist yet.
Connect to Your Database:
Click Connect on your cluster dashboard and select Connect your application.
Copy the connection string (e.g., mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority).
Replace <username>, <password>, and <dbname>:
Use the credentials you created during setup.
Replace <dbname> with jocko_assistant.

Connect to MongoDB Atlas (if not done already):
Why: This step is required to start working with the data in your JSON files using MongoDB.
Download MongoDB Compass (GUI) for connecting to MongoDB easily:
Go to MongoDB Compass Download.
Install it on your computer.
Connect:
Open Compass.
Use your MongoDB Atlas connection string (you can find it in your Atlas dashboard under "Clusters > Connect").
Follow the on-screen instructions in Compass to establish a connection.
2) Create Your Database:
Why: You’ll organize the data into collections, similar to tables in relational databases, so it’s easy to query later.
Once connected in Compass:
Click “Create Database”.
Name the database jocko_assistant.
Import JSON files to collections using Compass
Indexes Created
  - `books` Collection:
    - Text Index on `chapters.chapter`.
  - `quotes` Collection:
    - Text Index on `quote`.
  - `youtube` Collection:
    - Text Index on `content`.
Tested Queries
  - Retrieve quotes by keyword (`$regex` on `quote`).
  - Retrieve YouTube content by keyword (`$regex` on `content`).
  - Retrieve book chapters by title (`$regex` on `chapters.chapter`).
  Aggregations Tested
  - Count total documents in collections.
Transform the books collection to a chapter-level structure.
Steps:Converted each chapter into its own document with unique chapter_id and linked by book_id.
Imported transformed data into MongoDB.
Updated indexes:
Text Index: chapter_title.
Compound Index: book_id, chapter_id.
Tested queries:
Search chapter titles by keyword.
Retrieve chapters by book_id.
Aggregation to count chapters per book.
Outcome: The books collection is now optimized for chapter-level queries and ready for RAG workflows.

## Planned Improvements
A preprocessing script will be developed to automate this manual formatting step in the future. This script will:
Detect chapters and parts based on text patterns.
Automatically generate a structured .txt file ready for the format_book_txt_to_json.py script.
