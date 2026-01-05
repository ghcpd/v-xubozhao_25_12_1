@echo off
REM Test runner script for Backend Analytics Service
REM Runs pytest with comprehensive output and coverage reporting
REM Windows (PowerShell) version

echo ========================================
echo Backend Analytics Service - Test Runner
echo ========================================
echo.

REM Check if venv exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run pytest with verbose output and coverage
echo Running pytest test suite...
echo.
pytest tests/ -v --tb=short --color=yes -ra --cov=tests --cov-report=term-missing --cov-report=html

if errorlevel 1 (
    echo.
    echo ========================================
    echo Tests FAILED
    echo ========================================
    exit /b 1
)

echo.
echo ========================================
echo All Tests PASSED!
echo ========================================
echo.
echo Coverage report generated in htmlcov/index.html
echo View the detailed report by opening: htmlcov\index.html
echo.
