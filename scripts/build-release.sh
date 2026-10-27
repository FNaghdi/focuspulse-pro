#!/usr/bin/env bash
set -euo pipefail

mkdir -p release

python3 -m zipfile -c \
  release/focuspulse_pro_v1.0.0.zip \
  focuspulse_pro.html README.md

test -s release/focuspulse_pro_v1.0.0.zip
