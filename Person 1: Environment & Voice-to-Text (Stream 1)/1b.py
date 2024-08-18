# Import necessary libraries
import whisper
from transformers import pipeline
# Uncomment and import Tortoise API if needed
# from tortoise.api import TextToSpeech

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result['text']

# Sample usage
if __name__ == "__main__":
    # Provide the path to your audio file
    audio_file = "recordings2.m4a"
    try:
        transcribed_text = transcribe_audio(audio_file)
        print("Transcribed Text:", transcribed_text)
    except Exception as e:
        print(f"Error during transcription: {e}")

