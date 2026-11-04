from pathlib import Path
import pandas as pd

PRIVATE = Path("data/private")
df = pd.read_csv(PRIVATE / "segments_combined.csv")

df["words"] = df["text"].fillna("").str.split().str.len()
df["secs"] = (df["EndTimeMs"] - df["StartTimeMs"]) / 1000

stats = (df.groupby(["source_file", "speakerCode"]).agg(lines = ("words", "size"), words = ("words", "sum"), secs = ("secs", "sum")).round(0).reset_index())

stats["source_file"] = stats["source_file"].str.extract(r"(T\d+)", expand=False).fillna(stats["source_file"])

pd.set_option("display.max_rows", None)
print(stats.to_string(index=False))