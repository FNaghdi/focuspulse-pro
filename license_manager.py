#!/usr/bin/env python3
"""FocusPulse Pro v1.0.0 — Companion License Key Generator & Validator for Billixi."""

import re
import secrets
import string
import sys

KEY_PATTERN = re.compile(r"^BLX-PRO-2026-[A-Z0-9]{4}$")


def verify_key(key: str) -> bool:
    """Verify if a license key matches the FocusPulse Pro v1.0 entitlement format."""
    return bool(KEY_PATTERN.match(key.strip().upper()))


def generate_keys(count: int = 10) -> list[str]:
    """Generate a batch of unique FocusPulse Pro license keys for Billixi fulfillment."""
    alphabet = string.ascii_uppercase + string.digits
    keys = set()
    while len(keys) < count:
        suffix = "".join(secrets.choice(alphabet) for _ in range(4))
        keys.add(f"BLX-PRO-2026-{suffix}")
    return sorted(keys)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--verify":
        candidate = sys.argv[2] if len(sys.argv) > 2 else ""
        status = "VALID" if verify_key(candidate) else "INVALID"
        print(f"Key: {candidate} -> {status}")
    else:
        print("FocusPulse Pro v1.0 — Sample Generated License Keys:")
        for k in generate_keys(10):
            print(k)
