@echo off
echo Setting up Python virtual environment...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

REM Create the virtual environment in a folder named 'venv'
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Check if requirements.txt exists and install dependencies
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo No requirements.txt found. Skipping dependency installation.
)

echo Virtual environment setup complete. Type 'deactivate' to exit.
