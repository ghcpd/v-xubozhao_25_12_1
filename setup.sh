#!/usr/bin/env bash
set -euo pipefail

# Create venv in .venv, upgrade tools and install pinned dependencies
python -V
python -m venv .venv

# Activate (supports bash/PowerShell via fallback to pip in venv)
if [ -f "./.venv/bin/activate" ]; then
  source ./.venv/bin/activate
elif [ -f "./.venv/Scripts/Activate.ps1" ]; then
  echo "PowerShell venv activation detected; running pip via direct path"
fi

# Use venv pip directly for cross-shell compatibility
./.venv/Scripts/pip.exe install --upgrade pip setuptools wheel || 
  ./.venv/bin/pip install --upgrade pip setuptools wheel
./.venv/Scripts/pip.exe install -r requirements.txt || 
  ./.venv/bin/pip install -r requirements.txt

echo "Setup complete. Activate the venv with: source .venv/bin/activate (UNIX) or .\.venv\Scripts\Activate.ps1 (PowerShell)"
