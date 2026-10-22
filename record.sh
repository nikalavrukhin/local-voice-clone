#!/bin/bash
# Запись эталона голоса с микрофона. Останови через Ctrl+C или дождись таймера.
set -e
cd "$(dirname "$0")"
mkdir -p samples
SECONDS_LEN="${1:-20}"
OUT="samples/${2:-voice}.wav"
MIC="${MIC:-:1}"   # :1 — микрофон MacBook Air, :0 — iPhone

echo "Говори что-нибудь ровным голосом ${SECONDS_LEN} секунд. Запись пошла..."
ffmpeg -hide_banner -loglevel error -f avfoundation -i "$MIC" \
  -t "$SECONDS_LEN" -ar 22050 -ac 1 -y "$OUT"
echo "Эталон записан: $OUT"
