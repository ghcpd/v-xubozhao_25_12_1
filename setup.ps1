# Powershell friendly setup script
param(
    [string]$VenvDir = '.venv'
)

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python not found; please install Python 3.10+ and add to PATH"
    exit 1
}

$python = $python.Source
$pyVersion = & $python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
if ($pyVersion -lt '3.10.0') {
    Write-Error "Python 3.10+ required; found $pyVersion"
    exit 1
}

Write-Host "Creating venv at $VenvDir"
& $python -m venv $VenvDir

$venvPython = Join-Path $VenvDir 'Scripts\python.exe'
& $venvPython -m pip install --upgrade pip setuptools wheel
& $venvPython -m pip install -r requirements.txt

Write-Host "Setup complete. Activate venv: .\$VenvDir\Scripts\Activate.ps1"
