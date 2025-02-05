import requests
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
Tmdb_key = os.getenv("TMDB-API")
Movie_id_list= [157336, 550, 680]

#Base url
Base_url="https://api.themoviedb.org/3/movie"
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
#https://api.themoviedb.org/3/movie/550?api_key=
#function to load data from tmdb
def tmdb_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={Tmdb_key}&language=en-US"
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    return None

#function to load the wikipedia link
def wiki_data(movie_title):
    params={
        "action": "query",
        "format": "json",
        "title": movie_title,
        "prop": "info",
        "inprop": "url"
    }
    
    response= requests .get(WIKI_API_URL, params= params)
    data= response.json()#contains the link
    pages= data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        if "fullurl" in page_data:
            return page_data["fullurl"]
    return "https://en.wikipedia.org/wiki/Main_Page"




