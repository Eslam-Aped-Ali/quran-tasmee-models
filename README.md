# quran-tasmee-models

On-device models for the Tasmee' (recitation check) feature of the Yusr app.
The app downloads one model on demand and runs it fully offline with whisper.cpp.

| Asset | What |
|---|---|
| `quran-big-turbo-q5_0-r1.bin` | Full model: whisper-large-v3-turbo Quran fine-tune, q5_0 (~574 MB). Needs a powerful phone. |
| `quran-small-base-q8_0-r1.bin` | Small model: tarteel whisper-base Quran, q8_0 (~82 MB). Less accurate. |
| `silero-v6.2.0.bin` | Voice activity detector, always downloaded with either model. |
| `bench-r1.pcm` | 1:2 clip used to time the model on the phone. |
| `manifest.json` | Sizes, sha256s and tuning. The app reads `releases/latest/download/manifest.json`. |
| `NOTICE.txt` | Licences (Apache-2.0 models, MIT whisper.cpp / Silero). |

Model files live only as release assets, never in git. To rebuild: Actions → **Build models** → Run workflow.

To change only the manifest's platform flags (no rebuild): download the release's `manifest.json`,
run `python3 tools/set_platforms.py manifest.json`, and upload it back with
`gh release upload models-r1 manifest.json --clobber`. Since app builds after 2026-11-27 every phone
is offered both models whatever `enabled` says; `use_gpu` is read only from an entry with
`enabled: true` (else the CPU).
