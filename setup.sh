#!/usr/bin/env bash
set -euo pipefail

# setup.sh - Create venv and install dependencies for Python 3.10+
# Usage: ./setup.sh [venv_dir]

VENV_DIR=${1:-.venv}
PYTHON_COMMAND=${PYTHON:-python}

echo "Using Python: $PYTHON_COMMAND"
P_VERSION=$($PYTHON_COMMAND -c "import sys; print('.'.join(map(str, sys.version_info[:3])))")
PY_MAJOR=$($PYTHON_COMMAND -c "import sys; print(sys.version_info[0])")
PY_MINOR=$($PYTHON_COMMAND -c "import sys; print(sys.version_info[1])")

if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
  echo "Python 3.10 or newer is required. Found: $P_VERSION"
  exit 1
fi

echo "Creating virtual environment at $VENV_DIR"
$PYTHON_COMMAND -m venv "$VENV_DIR"

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python -m pip install -r requirements.txt

echo "Virtual environment ready. Activate with: source $VENV_DIR/bin/activate"
