#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON:-python3}"
VENV_DIR="${VENV_DIR:-.venv}"
REQ_FILE="${REQ_FILE:-requirements.txt}"

if [ ! -f "$REQ_FILE" ]; then
  echo "Requirements file '$REQ_FILE' not found" >&2
  exit 1
fi

# Create venv
$PYTHON_BIN -m venv "$VENV_DIR"

# Activate venv (POSIX or Windows under MSYS/WSL)
if [ -f "$VENV_DIR/bin/activate" ]; then
  # shellcheck disable=SC1090
  source "$VENV_DIR/bin/activate"
elif [ -f "$VENV_DIR/Scripts/activate" ]; then
  # shellcheck disable=SC1091
  source "$VENV_DIR/Scripts/activate"
else
  echo "Could not find activate script in $VENV_DIR" >&2
  exit 1
fi

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r "$REQ_FILE"

# Freeze for reproducibility
python -m pip freeze > requirements.lock

echo "Environment ready in '$VENV_DIR'."
