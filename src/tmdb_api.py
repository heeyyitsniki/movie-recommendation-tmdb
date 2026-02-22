import os
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/{}"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_id: int) -> str | None:
    if not movie_id:
        return None

    if not TMDB_API_KEY:
        print("TMDB_API_KEY is not set")
        return None
    else:
        print("Using TMDB_API_KEY:", TMDB_API_KEY[:4], "...")

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
    }

    try:
        response = requests.get(
            TMDB_MOVIE_URL.format(movie_id),
            params=params,
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")
        if not poster_path:
            return None

        full_url = f"{TMDB_IMAGE_BASE}{poster_path}"
        return full_url

    except Exception as e:
        print("Error in fetch_poster:", e)
        return None

'''
import os
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "722f14d76cd294538a109d3602a08eb6")

TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/{}"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_id: int) -> str | None:
    if not movie_id:
        print("NO MOVIE ID")
        return None

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
    }

    try:
        response = requests.get(TMDB_MOVIE_URL.format(movie_id), params=params, timeout=5)
        print("STATUS:", response.status_code, "URL:", response.url)
        response.raise_for_status()
        data = response.json()

        print("RAW JSON:", data)          # add this
        poster_path = data.get("poster_path")
        print("POSTER PATH:", poster_path)  # and this

        if not poster_path:
            return None

        full_url = f"{TMDB_IMAGE_BASE}{poster_path}"
        print("POSTER URL:", full_url)
        return full_url

    except Exception as e:
        print("Error in fetch_poster:", e)
        return None
'''