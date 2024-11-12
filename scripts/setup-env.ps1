# setup_venv.ps1

# Check if virtual environment folder exists
if (!(Test-Path -Path "./venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Virtual environment created."
} else {
    Write-Host "Virtual environment already exists."
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
if ($IsWindows) {
    .\venv\Scripts\Activate
} else {
    source venv/bin/activate
}

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Setup complete. To activate the virtual environment, use: .\venv\Scripts\Activate (Windows) or source venv/bin/activate (Mac/Linux)"
