#!/usr/bin/env python
"""Синтез речи голосом из эталонной записи (XTTS-v2, локально).

  python say.py "Привет, это мой голос"
  python say.py "Текст" --voice samples/voice.wav --out out/result.wav --lang ru
"""
import argparse
import os
import sys
from pathlib import Path

BASE = Path(__file__).parent
os.environ.setdefault("COQUI_TOS_AGREED", "1")

parser = argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("--voice", default=str(BASE / "samples" / "voice.wav"))
parser.add_argument("--out", default=str(BASE / "out" / "result.wav"))
parser.add_argument("--lang", default="ru")
parser.add_argument("--speed", type=float, default=1.0)
args = parser.parse_args()

voice = Path(args.voice)
if not voice.exists():
    sys.exit(f"Нет эталона голоса: {voice}\nЗапиши его: ./record.sh")

import torch
from TTS.api import TTS

device = "mps" if torch.backends.mps.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

Path(args.out).parent.mkdir(parents=True, exist_ok=True)
tts.tts_to_file(
    text=args.text,
    speaker_wav=str(voice),
    language=args.lang,
    file_path=args.out,
    speed=args.speed,
)
print(f"Готово: {args.out}")
