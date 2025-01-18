import whisper

# Load the pre-trained Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe(r"C:\Users\greyg\OpenAudible\books\TheDichotomyofLeadershipBalancingtheChallengesofExtremeOwnershiptoLeadandWin_ep7.mp3")

import os

# Save the transcription to a text file
output_path = os.path.join(os.getcwd(), "dichotomy_leadership.txt")
with open(output_path, "w") as f:
    f.write(result["text"])

print(f"Transcription complete. The text is saved in {output_path}.")