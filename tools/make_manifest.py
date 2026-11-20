"""Write manifest.json (schema 1) for the files in OUT_DIR, with real sizes and sha256s."""
import datetime
import hashlib
import json
import os
import sys

out = sys.argv[1]


def info(name):
    path = os.path.join(out, name)
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return {"file": name, "bytes": os.path.getsize(path), "sha256": h.hexdigest(), "mirrors": []}


def model(model_id, version, name, source, min_ram, rtf_ok, rtf_max):
    return {
        "id": model_id, "version": version, **info(name),
        "source": source, "licence": "Apache-2.0",
        "platforms": {"android": {"enabled": True, "use_gpu": False},
                      "ios": {"enabled": False, "use_gpu": True}},
        "min_ram_mb": min_ram, "threads": [2, 4],
        "rtf_ok": rtf_ok, "rtf_max": rtf_max, "interim_rtf": 0.3,
        "unclear_logprob": -0.6, "min_logprob": -1.0, "max_compression": 2.4,
        "max_phrase_s": 12.0, "fallback_full_window": True,
    }


manifest = {
    "schema": 1,
    "updated": datetime.date.today().isoformat(),
    "min_app_build": 1,
    "vad": {"version": "silero-v6.2.0", **info("silero-v6.2.0.bin")},
    "bench": {"version": "bench-r1", **info("bench-r1.pcm"),
              "sample_rate": 16000, "surah": 1, "ayah": 2},
    "models": [
        model("big", "turbo-q5_0-r1", "quran-big-turbo-q5_0-r1.bin",
              "naazimsnh02/whisper-large-v3-turbo-ar-quran@670f826", 5500, 0.5, 1.0),
        model("small", "base-q8_0-r1", "quran-small-base-q8_0-r1.bin",
              "tarteel-ai/whisper-base-ar-quran@5c3c53f", 2800, 0.3, 0.8),
    ],
}
print(json.dumps(manifest, indent=2, ensure_ascii=False))
