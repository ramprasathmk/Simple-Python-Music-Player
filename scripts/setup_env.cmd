#!/bin/bash

# Check if Python is installed
python --version >nul 2>&1
if errorlevel 1; then
    echo Python is not installed. Please install Python and try again.
    exit /b
fi

# Check if virtual environment folder exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. To activate the virtual environment, use: source venv/bin/activate"
