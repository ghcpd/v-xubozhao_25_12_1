#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Virtualenv not found - please run ./setup.sh first"
  exit 1
fi

# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

pytest -q
