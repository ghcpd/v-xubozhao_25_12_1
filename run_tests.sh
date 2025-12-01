#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=${1:-.venv}

if [ ! -d "$VENV_DIR" ]; then
  echo "Virtualenv $VENV_DIR not found. Run setup.sh first."
  exit 1
fi

# Activate venv
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# Run pytest with verbose and capture full output
pytest -q --disable-warnings --maxfail=1
