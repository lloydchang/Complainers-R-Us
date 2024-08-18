#!/bin/sh -x

# Initialize pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Set the Python version to 3.10.13 using pyenv
pyenv shell 3.10.13

# Check if pyenv successfully set the correct Python version
if ! python --version | grep -q "3.10.13"; then
  echo "Failed to set Python 3.10.13. Please ensure it is installed via pyenv."
  exit 1
fi

# Create a virtual environment
python -m venv .venv

# Check if the virtual environment was created successfully
if [ ! -d ".venv" ]; then
  echo "Failed to create the virtual environment."
  exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if the virtual environment was activated successfully
if [ ! "$VIRTUAL_ENV" ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

pip install --upgrade pip

# Install the required Python packages
pip install numba inflect psutil
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install transformers tokenizers --only-binary=:all:
pip install gtts git+https://github.com/wolph/python-progressbar pygame

# Clone the Tortoise TTS repository and install it
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
pip install .

echo "Setup completed successfully."
