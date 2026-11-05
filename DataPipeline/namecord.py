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
        found = [n in n in NAMES if n in text]
        for name in found:
            if i > 0:
                counts[(video, speakers[i-1], name)] +=1
            if i < len(speakers) - 1:
                counts[(video, speakers[i-1], name)] +=1

            out = pd.DataFrame([(v,s,n,c) for (v,s,n), c in counts.items()],
                            columns = ["video", "speaker", "name", "hits"])
            print(out.sort_values("hits", ascending= False).head(40).to_string(index=False))
                    #TO DO
        pass