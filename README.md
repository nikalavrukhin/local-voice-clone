# Local Voice Clone

Clone a voice from a ~20 second recording and synthesize speech in it, **fully offline** on a Mac (Apple Silicon, Metal/MPS) using Coqui XTTS-v2. Supports 16 languages, including Russian.

```bash
./record.sh 20                         # record a reference sample from the microphone -> samples/voice.wav
python say.py "Hello, this is my voice"
python say.py "Привет!" --lang ru --speed 1.1 --out out/hi.wav
```

**Setup notes**
- Python 3.12, `pip install -r requirements.txt` (`transformers` must be 4.x for coqui-tts).
- Model weights (~1.9 GB) are downloaded on first run.
- Reference recordings are git-ignored. Only clone voices you have permission to use.

Stack: Python, PyTorch (MPS), XTTS-v2, ffmpeg.
