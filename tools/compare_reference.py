"""Print whether the built files match the sha256s measured on the reference build.

A mismatch is reported, not fatal: the manifest always carries the real hashes.
"""
import sys

REFERENCE = {
    "quran-big-turbo-q5_0-r1.bin": "adda5cdd436c42908c82a5d86a808315d08d8cedfb90195837773f612b258ce2",
    "quran-small-base-q8_0-r1.bin": "72194195f7d280adebec57acf2c6e01e209484322ec1cec21c275a3c0b1e3d77",
    "silero-v6.2.0.bin": "2aa269b785eeb53a82983a20501ddf7c1d9c48e33ab63a41391ac6c9f7fb6987",
}

with open(sys.argv[1]) as f:
    for line in f:
        digest, name = line.split()
        ref = REFERENCE.get(name)
        if ref is None:
            continue
        print(f"{name}: {'matches reference' if digest == ref else 'DIFFERS from reference'}")
