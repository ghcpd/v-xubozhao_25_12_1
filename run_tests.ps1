# Automated pytest runner for backend analytics service (PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "================================================" -ForegroundColor Blue
Write-Host "   Backend Analytics Service - Test Suite" -ForegroundColor Blue
Write-Host "================================================" -ForegroundColor Blue
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Error: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Run '.\setup.ps1' first" -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Blue
& "venv\Scripts\Activate.ps1"

# Verify pytest is installed
try {
    $pytestVersion = pytest --version 2>&1
    Write-Host "✓ Environment activated" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "Error: pytest not found!" -ForegroundColor Red
    Write-Host "Run '.\setup.ps1' to install dependencies" -ForegroundColor Yellow
    exit 1
}

# Run pytest with verbose output
Write-Host "Running pytest test suite..." -ForegroundColor Blue
Write-Host ""

pytest tests/ `
    --verbose `
    --tb=short `
    --color=yes `
    --junit-xml=test-results.xml `
    -v

$testExitCode = $LASTEXITCODE

Write-Host ""
if ($testExitCode -eq 0) {
    Write-Host "================================================" -ForegroundColor Green
    Write-Host "   ✅ ALL TESTS PASSED" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Green
} else {
    Write-Host "================================================" -ForegroundColor Red
    Write-Host "   ❌ TESTS FAILED" -ForegroundColor Red
    Write-Host "================================================" -ForegroundColor Red
    exit $testExitCode
}

Write-Host ""
Write-Host "Test results saved to: test-results.xml" -ForegroundColor Blue
