import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_similarity(new_df):
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf.fit_transform(new_df["tags"].fillna(""))
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend(movie_title, new_df, similarity, top_n=10):
    titles_lower = new_df["title"].str.lower()
    movie_title = movie_title.strip().lower()

    if movie_title not in titles_lower.values:
        return []

    idx = titles_lower[titles_lower == movie_title].index[0]

    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1: top_n + 1]

    indices = [i[0] for i in sim_scores]
    return new_df["title"].iloc[indices].tolist()
