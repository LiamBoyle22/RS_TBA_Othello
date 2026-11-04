from pathlib import Path
from collections import Counter
import pandas as pd

NAMES = ["othello", "iago", "desdemona", "cassio", "emilia", "roderigo", "brabantio", "bianca", "lodovico", "monato", "gratiano"]

df = pd.read_csv(Path("data/private/segments_combined.csv"))
df = df.sort_values(["suorce_file", "position"])
counts = Counter()

for video, vdf in df.groupby("source_file"):
    speakers = vdf["SpeakerCode"].tolist()
    texts = vdf["text"].fillna("").str.lower().tolist()
    for i, text in enumerate(texts):
        #TO DO
        pass