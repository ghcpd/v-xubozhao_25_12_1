# Setup script for backend analytics service (PowerShell)
# Creates virtual environment and installs dependencies

$ErrorActionPreference = "Stop"

Write-Host "🚀 Setting up backend analytics environment..." -ForegroundColor Blue
Write-Host ""

# Check Python version
Write-Host "Checking Python version..." -ForegroundColor Blue
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion detected" -ForegroundColor Green
    
    # Check if Python 3.10+
    $versionMatch = $pythonVersion -match "Python (\d+)\.(\d+)"
    if ($versionMatch) {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
            Write-Host "Error: Python 3.10+ required. Found: $pythonVersion" -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "Error: Python not found or not in PATH" -ForegroundColor Red
    exit 1
}

# Remove old virtual environment if it exists
if (Test-Path "venv") {
    Write-Host "Removing old virtual environment..." -ForegroundColor Blue
    Remove-Item -Recurse -Force venv
}

# Create new virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Blue
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Blue
& "venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Blue
python -m pip install --upgrade pip setuptools wheel

# Install dependencies
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Blue
pip install -r requirements.txt

# Verify installation
Write-Host "Verifying installations..." -ForegroundColor Blue
python -c @"
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import scipy
import pytest
import fastapi
import uvicorn
print('✓ All core packages imported successfully')
print(f'  - numpy: {np.__version__}')
print(f'  - pandas: {pd.__version__}')
print(f'  - scikit-learn: {sklearn.__version__}')
print(f'  - pytest: {pytest.__version__}')
print(f'  - fastapi: {fastapi.__version__}')
"@

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To activate the environment, run:"
Write-Host "  .\venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "To run tests, execute:"
Write-Host "  .\run_tests.ps1"
