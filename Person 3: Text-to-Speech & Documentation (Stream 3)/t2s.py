import torch
from tortoise.api import TextToSpeech
import torchaudio

def changeTTS(resText):
    device = "cpu"  # Change to "cuda" if using a GPU
    print(f"Using device: {device}")

    print("Initializing Tortoise TTS...")
    tts = TextToSpeech(device=device)
    print("Tortoise TTS initialized successfully.")

    print(f"Generating speech for text: {resText}")
    # Generate speech using a default voice
    gen = tts.tts(resText, voice_samples=None, conditioning_latents=None)
    print("Speech generated successfully.")

    print("Saving audio...")
    torchaudio.save("output.wav", gen.squeeze(0).cpu(), 24000)
    print("Audio saved successfully.")

# Test the TTS function
if __name__ == "__main__":
    test_text = "This is a short test of Tortoise Text-to-Speech."
    print("Starting TTS test...")
    changeTTS(test_text)
    print("TTS test completed.")

