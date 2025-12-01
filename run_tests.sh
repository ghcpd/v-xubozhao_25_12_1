#!/bin/bash

# Automated pytest runner for backend analytics service

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   Backend Analytics Service - Test Suite${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Error: Virtual environment not found!${NC}"
    echo -e "${YELLOW}Run 'bash setup.sh' first${NC}"
    exit 1
fi

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Verify pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}Error: pytest not found!${NC}"
    echo -e "${YELLOW}Run 'bash setup.sh' to install dependencies${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Environment activated${NC}"
echo ""

# Run pytest with verbose output and coverage
echo -e "${BLUE}Running pytest test suite...${NC}"
echo ""

pytest tests/ \
    --verbose \
    --tb=short \
    --color=yes \
    --junit-xml=test-results.xml \
    -v

TEST_EXIT_CODE=$?

echo ""
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}================================================${NC}"
    echo -e "${GREEN}   ✅ ALL TESTS PASSED${NC}"
    echo -e "${GREEN}================================================${NC}"
else
    echo -e "${RED}================================================${NC}"
    echo -e "${RED}   ❌ TESTS FAILED${NC}"
    echo -e "${RED}================================================${NC}"
    exit $TEST_EXIT_CODE
fi

echo ""
echo -e "${BLUE}Test results saved to: test-results.xml${NC}"
