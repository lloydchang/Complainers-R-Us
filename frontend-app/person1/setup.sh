#!/bin/sh -x
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt update
sudo apt install python3-pip
pip install -r requirements.txt

# Create and activate a virtual environment (optional)
# python3 -m venv env
# source env/bin/activate  # On Linux and macOS
# # .\env\Scripts\activate  # On Windows

# Install FastAPI and Uvicorn
pip install fastapi uvicorn
