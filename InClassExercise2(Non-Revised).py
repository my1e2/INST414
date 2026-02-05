import json
import pandas as pd
from collections import Counter

data = []

with open("imdb_movies_2000to2022.prolific.json", "r") as file_connection:
    for line in file_connection:
        data.append(json.loads(line))
print(data)

df = pd.DataFrame
print(df)

actor_counts = Counter()
for cast in df['actors'].dropna():
    actor_counts.update([a[1]for a in cast])
top_actors = actor_counts.most_common(10)
actors_df = pd.DataFrame(top_actors, columns = ["Actors", "Count"])
print(actors_df.to_string(index=False))



genre_counts = Counter()
for genre in df["genres"].dropna():
    genre_counts.update([g in genres if g!="\\N"])
top_genres = genre_counts.most_common(10)
genres_df = pd.DataFrame(top_genres, columns = ["Genre", "Count"])
print(genres_df.to_string(index=False))


df_rated = df.dropna(subset=["rating"]).copy

df_rated["avg_rating"] = df_rated["rating"].apply(lambda r: r.get("avg") if isinstance(r, dict)else None)

top_rated = (df_rated.dropna(subset = ["avg_rating"]).sort_values("avg_rating", ascending = False).head(10))

print(top_rated[["title", "avg_rating"]].to_string(index =False))

df_rated["votes"] = df_rated["rating"].apply(lambda r: r.get("avg") if isinstance(r, dict)else None)

top_votes = (df_rated.dropna(subset = ["votes"]).sort_values("votes", ascending = False).head(10))

print(top_rated[["title", "votes"]].to_string(index =False))