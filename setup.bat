@echo off
REM Setup script for Backend Analytics Service
REM Creates virtual environment and installs all dependencies
REM Windows (PowerShell) version

echo ========================================
echo Backend Analytics Service - Setup
echo ========================================
echo.

REM Check Python version
python --version
python -c "import sys; assert sys.version_info >= (3, 10), 'Python 3.10+ required'"
if errorlevel 1 (
    echo ERROR: Python 3.10+ is required
    exit /b 1
)

REM Remove existing venv if it exists
if exist venv (
    echo Removing existing virtual environment...
    rmdir /s /q venv
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip
    exit /b 1
)

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    exit /b 1
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To activate the environment in future sessions, run:
echo   venv\Scripts\activate.bat
echo.
echo To run tests, execute:
echo   run_tests.bat
echo.
