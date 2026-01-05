#!/usr/bin/env bash
set -euo pipefail

# Prefer using venv pip/pytest; if not present, try activating venv
if [ -f "./.venv/Scripts/Activate.ps1" ] || [ -f "./.venv/bin/activate" ]; then
  echo "Using venv at ./.venv"
  if [ -f "./.venv/Scripts/pytest.exe" ]; then
    ./.venv/Scripts/pytest.exe -q --maxfail=1
  elif [ -f "./.venv/Scripts/python.exe" ]; then
    ./.venv/Scripts/python.exe -m pytest -q --maxfail=1
  else
    ./.venv/bin/python -m pytest -q --maxfail=1
  fi
else
  echo "No venv found - running pytest from system python (may not match pinned environment)"
  python -m pytest -q --maxfail=1
fi

