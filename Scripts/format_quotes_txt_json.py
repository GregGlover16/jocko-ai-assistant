import json

# Input and output file paths
input_file_path = "Jocko Motivational Quotes.txt"
output_file_path = "jocko_quotes.json"

def parse_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Create a list of quote objects
    quotes = [{"quote": line.strip()} for line in lines if line.strip()]  # Skip empty lines
    return quotes

def save_quotes_to_json(quotes, output_path):
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(quotes, json_file, indent=4, ensure_ascii=False)
    print(f"Quotes have been successfully saved to {output_path}")

# Main function
def main():
    quotes = parse_quotes(input_file_path)
    save_quotes_to_json(quotes, output_file_path)

if __name__ == "__main__":
    main()
