#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="${VENV_DIR:-.venv}"
PYTEST_ARGS=${PYTEST_ARGS:-"-q --disable-warnings --maxfail=1"}

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

python -m pytest $PYTEST_ARGS
