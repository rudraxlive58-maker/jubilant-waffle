"""Basic SHA-256 tamper-evidence check for the UNFAIR source files.
This detects unexpected edits; it is not DRM or protection against a skilled editor.
"""
from hashlib import sha256
from pathlib import Path
import sys

# Filled by the build step after main.py and bot_core.py are finalized.
EXPECTED = {
    "main.py": "0003303c6b8ebacee8a22f7218d3d26aafcf99306f460d588cc5c990cc59bb03",
    "bot_core.py": "74b70a0044fc2159ecd15cdbc4d5a7e126a2f32b3d34cb50e37649e33de1e05b",
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

