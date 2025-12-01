#!/usr/bin/env bash
set -euo pipefail

# Create a reproducible venv and install dependencies
VENV_DIR=".venv"
PYTHON=${PYTHON:-python3}

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Python not found: $PYTHON" >&2
  exit 1
fi

# Verify Python version >= 3.10
PY_VER=$($PYTHON -c "import sys; print('.'.join(map(str, sys.version_info[:3])))")
PY_MAJOR=$($PYTHON -c "import sys; print(sys.version_info.major)")
PY_MINOR=$($PYTHON -c "import sys; print(sys.version_info.minor)")

if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
  echo "Python 3.10+ required. Detected version: $PY_VER" >&2
  exit 1
fi

# Create venv
if [ ! -d "$VENV_DIR" ]; then
  $PYTHON -m venv "$VENV_DIR"
fi

# Activate venv and pip install
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

pip install --upgrade pip
pip install -r requirements.txt

# Ensure pytest is installed
pip install pytest

cat <<'EOF'
Setup complete. Activate the venv with:
  source .venv/bin/activate
Then run tests with:
  ./run_tests.sh
EOF
