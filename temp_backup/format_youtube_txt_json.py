import json

# Input and output file paths
input_file_path = "Jocko Youtube videos.txt"
output_file_path = "jocko_youtube_transcripts.json"

def parse_transcripts(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    formatted_transcripts = []
    current_title = None
    current_content = []

    for line in lines:
        stripped_line = line.strip()

        # Identify a title (lines starting with *** and ending with ***)
        if stripped_line.startswith("***") and stripped_line.endswith("***"):
            # If there's an existing title, save its content before starting a new section
            if current_title and current_content:
                formatted_transcripts.append({
                    "title": current_title.strip("*"),  # Remove asterisks from the title
                    "content": " ".join(current_content).strip(),  # Join content lines
                    "tags": [],  # Placeholder for tags
                    "source": "YouTube"
                })
                current_content = []  # Reset content for the new section

            current_title = stripped_line  # Set the new title
        elif stripped_line:  # Content line (non-empty and not a title)
            current_content.append(stripped_line)
        # Blank lines are ignored in this structure

    # Add the last section after the loop finishes
    if current_title and current_content:
        formatted_transcripts.append({
            "title": current_title.strip("*"),
            "content": " ".join(current_content).strip(),
            "tags": [],
            "source": "YouTube"
        })

    return formatted_transcripts

def save_transcripts_to_json(transcripts, output_path):
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(transcripts, json_file, indent=4, ensure_ascii=False)
    print(f"Transcripts have been successfully saved to {output_path}")

# Main function
def main():
    transcripts = parse_transcripts(input_file_path)
    save_transcripts_to_json(transcripts, output_file_path)

if __name__ == "__main__":
    main()


