"""Build Klox app icons from the approved master PNG (issue #58).
Usage: python3 tools/make-icons.py path/to/klox-icon.png
Warns if the master is not the original Drive file (a WhatsApp copy is
re-encoded, so its sha256 differs), then writes the icon set to the repo root."""
import hashlib, sys, pathlib
from PIL import Image

EXPECTED = "3a1e1a36b90137e4314c916b9df7fc2ff5bed911e19baf30fb551bc4e29ad28f"
src = pathlib.Path(sys.argv[1])
digest = hashlib.sha256(src.read_bytes()).hexdigest()
if digest != EXPECTED:
    print(f"note: sha256 {digest} is not the Drive original (re-encoded copy?)")
root = pathlib.Path(__file__).resolve().parent.parent
master = Image.open(src).convert("RGBA")
def out(size, name):
    master.resize((size, size), Image.LANCZOS).save(root / name, optimize=True)
out(16, "favicon-16.png")
out(32, "favicon-32.png")
out(180, "apple-touch-icon.png")
out(192, "icon-192.png")
out(512, "icon-512.png")
master.resize((256, 256), Image.LANCZOS).save(root / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("icons written")
