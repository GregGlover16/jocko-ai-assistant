import json
import re

# Path to the reformatted .txt file
file_path = "dichotomy_leadership.txt"

# Output JSON file path
output_path = "dichotomy_leadership.json"

# Function to parse parts, introduction, and chapters
def parse_parts_and_chapters(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Split text by "Part X - [Title]" to isolate each part
    parts = re.split(r"(Part \w+ - .+)", text)

    formatted_parts = []
    intro_content = None  # To capture content before "Part I"

    if not parts[0].strip().startswith("Part"):  # Check for intro or pre-part content
        intro_content = parts[0].strip()
        parts = parts[1:]  # Remove the introduction section from the parts list

    for i in range(0, len(parts), 2):  # Step through parts
        part_title = parts[i].strip()  # "Part X - Title"
        part_body = parts[i + 1].strip()  # Content within the part

        # Split part body into chapters by "Chapter X."
        chapters = re.split(r"(Chapter \d+\.)", part_body)

        formatted_chapters = []
        for j in range(1, len(chapters), 2):  # Step through chapters
            chapter_heading = chapters[j].strip()  # "Chapter X."
            chapter_body = chapters[j + 1].strip()  # Content following the chapter heading

            # Extract the chapter title and content
            lines = chapter_body.split("\n", 1)
            chapter_title = lines[0].strip()  # First line as title
            content = lines[1].strip() if len(lines) > 1 else ""  # Remaining lines as content

            # Structure chapter JSON
            chapter_data = {
                "chapter": f"{chapter_heading} {chapter_title}",  # Combine heading and title
                "content": content,  # Rest of the chapter text
                "summary": ""  # Placeholder for summaries
            }
            formatted_chapters.append(chapter_data)

        # Structure part JSON
        part_data = {
            "part_title": part_title,  # Title of the part
            "chapters": formatted_chapters  # List of chapters in the part
        }
        formatted_parts.append(part_data)

    # Add introduction as a "Part 0" if intro_content exists
    if intro_content:
        intro_chapters = re.split(r"(Chapter \d+\.)", intro_content)
        intro_formatted_chapters = []

        for k in range(1, len(intro_chapters), 2):
            chapter_heading = intro_chapters[k].strip()
            chapter_body = intro_chapters[k + 1].strip()
            lines = chapter_body.split("\n", 1)
            chapter_title = lines[0].strip()
            content = lines[1].strip() if len(lines) > 1 else ""

            intro_formatted_chapters.append({
                "chapter": f"{chapter_heading} {chapter_title}",
                "content": content,
                "summary": ""
            })

        formatted_parts.insert(0, {
            "part_title": "Part 0 - Introduction",
            "chapters": intro_formatted_chapters
        })

    return formatted_parts

# Main function to format and save the book as JSON
def format_book_with_parts_and_chapters():
    formatted_parts = parse_parts_and_chapters(file_path)
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(formatted_parts, json_file, indent=4)
    print(f"Book formatted and saved to {output_path}")

# Execute the script
format_book_with_parts_and_chapters()








