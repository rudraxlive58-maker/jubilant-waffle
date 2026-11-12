"""Basic SHA-256 tamper-evidence check for the UNFAIR source files.
This detects unexpected edits; it is not DRM or protection against a skilled editor.
"""
from hashlib import sha256
from pathlib import Path
import sys

# Filled by the build step after main.py and bot_core.py are finalized.
EXPECTED = {
    "main.py": "8a7a065619e4f02700909e50f00370ceceda65c5c4b3dbb8b3aaab763eaaee11",
    "bot_core.py": "e1a56b8f9ba2074bc1656a45a1e3765ad7aaf13eeb94a8e3c875cc8a992a4a21",
}

def verify_integrity(folder=None):
    base = Path(folder) if folder else Path(__file__).resolve().parent
    failures = []
    for filename, expected in EXPECTED.items():
        target = base / filename
        if not target.is_file():
            failures.append(f"{filename}: missing")
            continue
        actual = sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            failures.append(f"{filename}: checksum mismatch")
    if failures:
        print("[UNFAIR SECURITY] Source integrity check failed:")
        for item in failures:
            print(" -", item)
        print("Files changed or missing. Restore the original files before running.")
        raise SystemExit(1)
    return True
