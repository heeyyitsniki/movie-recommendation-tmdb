import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_similarity(df: pd.DataFrame):
    """
    Build a cosine-similarity matrix on TMDB 'tags' column.
    df must contain at least: 'title', 'tags'.
    """
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df["tags"].fillna(""))
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend(selected_movie, movies, similarity, n=5):
    movie_index = movies[movies["title"] == selected_movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:n+1]

    recommended_names = []
    recommended_indices = []

    for i, _score in movie_list:
        recommended_indices.append(i)
        recommended_names.append(movies.iloc[i].title)

    return recommended_names, recommended_indices
