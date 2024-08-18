from gtts import gTTS
import io
import pygame

def play_audio_with_pygame(tts_audio):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio data into pygame
    pygame.mixer.music.load(tts_audio)
    
    # Play the audio
    pygame.mixer.music.play()
    
    # Keep the program running until the sound finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Prevent the program from exiting until the audio finishes

def changeTTS(resText, lang="en", slow=False):
    # Initialize gTTS object
    tts = gTTS(text=resText, lang=lang, slow=slow)
    
    # Save the gTTS output to a BytesIO object (in-memory file)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    
    # Rewind the buffer's position to the beginning
    audio_buffer.seek(0)
    
    # Play the sound using pygame
    play_audio_with_pygame(audio_buffer)

# # Example usage
# text_to_test = "Hello! This is a test of the Google Text-to-Speech library."
# changeTTS(text_to_test)

#Tortoise that doesn't work
# import torch
# from tortoise.api import TextToSpeech
# import torchaudio

# # Force CPU usage
# device = "cpu"
# print(f"Using device: {device}")

# # Initialize Tortoise TTS
# print("Initializing Tortoise TTS...")
# tts = TextToSpeech(device=device)
# print("Tortoise TTS initialized successfully.")

# def changeTTS(resText):
#     print(f"Generating speech for text: {resText}")
#     # Generate speech using a default voice
#     gen = tts.tts(resText, voice_samples=None, conditioning_latents=None)
#     print("Speech generated successfully.")

#     print("Saving audio...")
#     torchaudio.save("output.wav", gen.squeeze(0).cpu(), 24000)
#     print("Audio saved successfully.")

# # Test the TTS function
# if __name__ == "__main__":
#     test_text = "This is a short test of Tortoise Text-to-Speech."
#     print("Starting TTS test...")
#     changeTTS(test_text)
#     print("TTS test completed.")