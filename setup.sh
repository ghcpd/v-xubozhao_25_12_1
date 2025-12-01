#!/bin/bash

# Setup script for backend analytics service
# Creates virtual environment and installs dependencies

set -e  # Exit on error

echo "🚀 Setting up backend analytics environment..."

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}Checking Python version...${NC}"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.10"

if ! python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)"; then
    echo -e "${RED}Error: Python 3.10+ required. Found: ${PYTHON_VERSION}${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Python ${PYTHON_VERSION} detected${NC}"

# Remove old virtual environment if it exists
if [ -d "venv" ]; then
    echo -e "${BLUE}Removing old virtual environment...${NC}"
    rm -rf venv
fi

# Create new virtual environment
echo -e "${BLUE}Creating virtual environment...${NC}"
python3 -m venv venv

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip setuptools wheel

# Install dependencies
echo -e "${BLUE}Installing dependencies from requirements.txt...${NC}"
pip install -r requirements.txt

# Verify installation
echo -e "${BLUE}Verifying installations...${NC}"
python3 -c "
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
"

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "To activate the environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests, execute:"
echo "  bash run_tests.sh"
