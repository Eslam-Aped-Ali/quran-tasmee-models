"""Set max_length = max_target_positions (448) in a Whisper HF config.json."""
import json
import sys

path = sys.argv[1]
with open(path) as f:
    cfg = json.load(f)
cfg["max_length"] = cfg["max_target_positions"]
with open(path, "w") as f:
    json.dump(cfg, f, indent=2)
print(f"max_length -> {cfg['max_length']}")
