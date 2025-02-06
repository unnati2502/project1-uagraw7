import requests
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
Tmdb_key = os.getenv("TMDB-API")
Movie_id_list = [
    1241982,762509,402431,1011985,748783,519182,1022789,808,109445,62177
    ]

Base_url="https://api.themoviedb.org/3/movie"
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

#function to load data from tmdb
def tmdb_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={Tmdb_key}&language=en-US"
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    return None

#function to load the wikipedia link
def wiki_data(movie_title):
    
    params = {
        "action": "query",
        "format": "json",
        "titles": movie_title,  
        "prop": "info",
        "inprop": "url",
        "formatversion": 2
    }

    response = requests.get(WIKI_API_URL, params=params)

    if response.status_code != 200:
        return "https://en.wikipedia.org/wiki/Main_Page"

    data = response.json()
    pages = data.get("query", {}).get("pages", [])

    if pages and "fullurl" in pages[0]:  # Extract Wikipedia URL
        return pages[0]["fullurl"]

    return "https://en.wikipedia.org/wiki/Main_Page"

        




