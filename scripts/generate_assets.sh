#!/usr/bin/env bash
set -euo pipefail

# Generates placeholder PNG assets for the project.
# Usage: ./scripts/generate_assets.sh

PY=$(which python3 || true)
if [ -z "$PY" ]; then
  echo "python3 not found. Please install Python 3 to generate assets." >&2
  exit 1
fi

DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Generating placeholder PNGs in $DIR/assets/images/ ..."

"$PY" "$DIR/tools/generate_placeholders.py"

echo "Done. You can now add the PNGs to a Defold atlas (e.g. atlases/game.atlas)."
