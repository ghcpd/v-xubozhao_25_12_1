#!/usr/bin/env bash
# Test runner script for Backend Analytics Service
# Runs pytest with comprehensive output and coverage reporting
# Linux/macOS version

set -e

echo "========================================"
echo "Backend Analytics Service - Test Runner"
echo "========================================"
echo

# Check if venv exists
if [ ! -d venv ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run setup.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run pytest with verbose output and coverage
echo "Running pytest test suite..."
echo

pytest tests/ -v --tb=short --color=yes -ra --cov=tests --cov-report=term-missing --cov-report=html

if [ $? -ne 0 ]; then
    echo
    echo "========================================"
    echo "Tests FAILED"
    echo "========================================"
    exit 1
fi

echo
echo "========================================"
echo "All Tests PASSED!"
echo "========================================"
echo
echo "Coverage report generated in htmlcov/index.html"
echo "View the detailed report by opening: htmlcov/index.html"
echo
