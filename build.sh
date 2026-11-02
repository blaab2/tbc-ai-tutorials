#!/usr/bin/env bash
# Baut die HTML-Version des Tutorials.  Aufruf:  ./build.sh   oder   ./build.sh --serve
set -euo pipefail
cd "$(dirname "$0")"
UV="$(command -v uv || echo ./.tools/uv)"
export UV_CACHE_DIR="${UV_CACHE_DIR:-$PWD/.tools/cache}"
export UV_PYTHON_INSTALL_DIR="${UV_PYTHON_INSTALL_DIR:-$PWD/.tools/python}"
exec "$UV" run build_html.py "$@"
