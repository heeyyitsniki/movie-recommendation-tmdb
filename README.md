# movie-recommendation-tmdb
Major Machine Learning Project on Movie Recommendation System using TMDB 5000 dataset.
 
## Project Description
This project is an end-to-end Movie Recommendation System that suggests similar movies using **content-based filtering** on the TMDB 5000 dataset (movies + credits). The raw CSV files are cleaned and merged, and a `tags` feature is created from genres, keywords, cast, crew, and overview, on which a TF–IDF vectorizer and cosine similarity are applied to compute movie–movie similarity. A Streamlit web app allows users to select a movie and get top-N similar recommendations, while posters are fetched dynamically from the TMDB API using a secure API key stored in environment variables/Streamlit Secrets. The codebase is modular with separate modules for data preparation, recommendation logic, and TMDB integration, and the app is deployed on Streamlit Community Cloud via a GitHub repository.
