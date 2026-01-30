import streamlit as st
from src.data_prep import get_new_df
from src.recommend import build_similarity, recommend

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

@st.cache_data
def load_data():
    return get_new_df()

@st.cache_resource
def load_model(df):
    return build_similarity(df)

def main():
    # --- Title (centered, like Figma) ---
    st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)

    st.write("")  # small gap

    # --- Subtitle text ---
    st.subheader("How you would like to be recommended?")

    # --- Load data and model ---
    df = load_data()
    similarity = load_model(df)

    # --- Dropdown for movie names ---
    movie_list = sorted(df["title"].unique().tolist())
    selected_movie = st.selectbox("Movie names dropdown", movie_list)

    # --- Recommend button ---
    if st.button("Recommend"):
        recs = recommend(selected_movie, df, similarity, top_n=5)

        if not recs:
            st.warning("No recommendations found.")
            return

        st.write("")  # gap

        # --- Show 5 recommended movies in a row (like cards) ---
        st.subheader("Recommended movies:")

        cols = st.columns(5)
        for i, title in enumerate(recs):
            with cols[i]:
                st.write(f"**Movie Name {i+1}**")
                st.write(title)

if __name__ == "__main__":
    main()
