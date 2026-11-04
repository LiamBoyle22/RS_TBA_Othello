from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
PRIVATE = ROOT / "data" / "private"

files = sorted(f for f in PRIVATE.glob("*.csv") if f.name != "segments_combined.csv")

frames = []
for f in files:
    df = pd.read_csv(f)
    df["source_file"] = f.name
    frames.append(df)

speakers = df["SpeakerCode"].nunique() if "SpeakerCode" in df else "n/a"
print(f" {f.name}: {len(df)} rows, {speakers} speakers")

all_df = pd.concat(frames, ignore_index=True)
print(all_df.shape, list(all_df.columns))
all_df.to_csv(PRIVATE / "segemnts_combined.csv", index=FALSE)