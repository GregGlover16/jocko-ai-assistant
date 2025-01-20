# Jocko AI Assistant
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
Chapterr 1. Taking Ownership
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

## Planned Improvements
A preprocessing script will be developed to automate this manual formatting step in the future. This script will:
Detect chapters and parts based on text patterns.
Automatically generate a structured .txt file ready for the format_book_txt_to_json.py script.
