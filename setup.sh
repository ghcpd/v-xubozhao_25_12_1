#!/usr/bin/env bash
# Setup script for Backend Analytics Service
# Creates virtual environment and installs all dependencies
# Linux/macOS version

set -e

echo "========================================"
echo "Backend Analytics Service - Setup"
echo "========================================"
echo

# Check Python version
python3 --version
python3 -c "import sys; assert sys.version_info >= (3, 10), 'Python 3.10+ required'"

# Remove existing venv if it exists
if [ -d venv ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo
echo "To activate the environment in future sessions, run:"
echo "  source venv/bin/activate"
echo
echo "To run tests, execute:"
echo "  bash run_tests.sh"
echo
