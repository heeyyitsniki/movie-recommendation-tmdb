import pickle
import streamlit as st

from src.recommend import recommend
from src.tmdb_api import fetch_poster

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations with posters.")


@st.cache_data
def load_data():
    # movies dataframe: must contain at least 'movie_id' and 'title'
    with open("artifacts_movies.pkl", "rb") as f:
        movies = pickle.load(f)
    return movies


@st.cache_resource
def load_model():
    # cosine similarity matrix
    with open("artifacts_similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return similarity


def main():
    movies = load_data()
    similarity = load_model()

    movie_list = movies["title"].values

    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list,
    )

    if st.button("Recommend"):
        # returns: names, indices
        names, indices = recommend(selected_movie, movies, similarity)

        cols = st.columns(5)
        for idx, col in enumerate(cols):
            if idx < len(indices):
                movie_index = indices[idx]
                movie_id = movies.iloc[movie_index].movie_id
                poster_url = fetch_poster(int(movie_id))

                with col:
                    st.caption(names[idx])
                    if poster_url:
                        st.image(poster_url, width="content")
                    else:
                        st.write("(No poster available)")

    st.markdown(
        """
        <hr>
        <p style="text-align:center; color:gray; font-size:14px;">
        Developed by <b>Team ML4TECH</b>
        </p>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
