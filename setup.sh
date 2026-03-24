#!/bin/zsh

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "Creating virtual environment in $VENV_DIR"
"$PYTHON_BIN" -m venv "$VENV_DIR"

echo "Installing dependencies from requirements.txt"
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install -r "$PROJECT_DIR/requirements.txt"

echo
echo "Done. Activate with:"
echo "source \"$VENV_DIR/bin/activate\""
