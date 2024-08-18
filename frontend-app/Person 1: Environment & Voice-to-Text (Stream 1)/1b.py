# Import necessary libraries
import whisper
from transformers import pipeline
from fastapi import FastAPI, File, UploadFile
# Uncomment and import Tortoise API if needed
# from tortoise.api import TextToSpeech

app = FastAPI()

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result['text']


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    try:
        audio_data = await file.read()
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_data)
        transcribed_text = transcribe_audio("temp_audio.wav")
        return JSONResponse(content={"transcribed_text": transcribed_text})
    except Exception as e:
        return JSONResponse(content={"error": f"Error during transcription: {e}"}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # Sample usage
    # Provide the path to your audio file
    # audio_file = "recordings2.m4a"
    # try:
    #     transcribed_text = transcribe_audio(audio_file)
    #     print("Transcribed Text:", transcribed_text)
    # except Exception as e:
    #     print(f"Error during transcription: {e}")

