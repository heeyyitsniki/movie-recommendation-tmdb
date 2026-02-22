import pickle
from src.data_prep import get_new_df
from src.recommend import build_similarity

def main():
    df = get_new_df()                 # your TMDB movies with tags
    similarity = build_similarity(df) # cosine similarity matrix

    with open("artifacts_movies.pkl", "wb") as f:
        pickle.dump(df, f)

    with open("artifacts_similarity.pkl", "wb") as f:
        pickle.dump(similarity, f)

    print("Saved artifacts_movies.pkl and artifacts_similarity.pkl")

if __name__ == "__main__":
    main()


