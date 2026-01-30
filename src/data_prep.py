import numpy as np
import pandas as pd
movies = pd.read_csv(r'C:\Users\mitali\OneDrive\Documents\GitHub\movie-recommendation-tmdb\data\tmdb_5000_credits.csv')
credits = pd.read_csv(r'C:\Users\mitali\OneDrive\Documents\GitHub\movie-recommendation-tmdb\data\tmdb_5000_movies.csv')

movies = movies.merge(credits, on = 'title')

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

#extracting name values from dictionary
import ast
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L
movies['cast'] = movies['cast'].apply(convert3)

def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L
movies['crew'] = movies['crew'].apply(convert3)

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ", " ") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ", " ") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ", " ") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ", " ") for i in x])

movies['tags'] = movies['overview']+ movies['genres']+ movies['keywords']+ movies['cast']+ movies['crew']

def get_new_df():
    new_df = movies[['movie_id', 'title', 'tags']]
    new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

    return new_df
