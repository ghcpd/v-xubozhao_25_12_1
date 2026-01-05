param(
    [string]$VenvDir = '.venv'
)

$venvPython = Join-Path $VenvDir 'Scripts\python.exe'
if (-not (Test-Path $venvPython)) {
    Write-Error "Virtualenv not found. Run setup.ps1 first."
    exit 1
}

& $venvPython -m pytest -q
