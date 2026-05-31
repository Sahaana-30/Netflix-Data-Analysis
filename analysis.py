import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv/netflix_titles.csv")

df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("movies_vs_tvshows.png")
plt.show()
