"""Rewrite the platform flags of an existing manifest.json in place, without rebuilding the models.

    gh release download models-r1 -p manifest.json -D out --clobber
    python3 tools/set_platforms.py out/manifest.json
    gh release upload models-r1 out/manifest.json --clobber

Sets every model to android {enabled: true, use_gpu: false} and ios {enabled: true, use_gpu: false}
(the values tools/make_manifest.py writes) and bumps "updated". Sizes and sha256s are left as they are.
"""
import datetime
import json
import sys

PLATFORMS = {"android": {"enabled": True, "use_gpu": False},
             "ios": {"enabled": True, "use_gpu": False}}

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    manifest = json.load(f)
for model in manifest["models"]:
    model["platforms"] = json.loads(json.dumps(PLATFORMS))
manifest["updated"] = datetime.date.today().isoformat()
with open(path, "w", encoding="utf-8") as f:
    f.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print("\n".join(f"{m['id']}: {m['platforms']}" for m in manifest["models"]))
