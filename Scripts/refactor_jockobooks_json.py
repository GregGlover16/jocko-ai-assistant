import json
import uuid

# Load existing data
with open("extreme_ownership_backup.json", "r") as f:
    books_data = json.load(f)

# Transform to chapter-level documents
transformed_data = []
for book in books_data:
    book_id = str(uuid.uuid4())  # Generate a unique book_id
    for chapter in book["chapters"]:
        chapter_doc = {
            "book_id": book_id,
            "book_title": book["book_title"],
            "chapter_id": str(uuid.uuid4()),  # Generate a unique chapter_id
            "chapter_title": chapter["chapter_title"],
            "content": chapter["content"]
        }
        transformed_data.append(chapter_doc)

# Save transformed data
with open("extreme_ownership.json", "w") as f:
    json.dump(transformed_data, f, indent=4)
