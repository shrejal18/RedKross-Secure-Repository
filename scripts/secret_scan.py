"""Basic secret-pattern scanner for the training repository."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(
        r"""(?i)(api_key|secret_key|password)\s*[:=]\s*['"][^'"]{8,}['"]"""
    ),
]

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
SKIP_FILES = {".env.example"}

findings = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if any(part in SKIP_DIRS for part in path.parts):
        continue

    if path.name in SKIP_FILES:
        continue

    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue

    for number, line in enumerate(content.splitlines(), start=1):
        if any(pattern.search(line) for pattern in PATTERNS):
            findings.append(f"{path.relative_to(ROOT)}:{number}")

if findings:
    print("Potential secrets detected:")
    for finding in findings:
        print(finding)
    raise SystemExit(1)

print("Secret scan passed. No matching patterns found.")