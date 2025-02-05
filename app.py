import flask
from flask import render_template
import random
from movie import tmdb_data, wiki_data, Movie_id_list
app= flask.Flask(__name__)

@app.route("/")
def main():
    movie_id= random.choice(Movie_id_list)
    movie_data= tmdb_data(movie_id)
    if movie_data:
        title= movie_data["original_title"]
        tagline=movie_data["tagline"]
        genre= movie_data["genres"]["name"]
        poster_path= movie_data["poster_path"]
        poster_url=f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
        wiki_url= wiki_data(title)
        
        return render_template('index.html', title= title, tagline= tagline,genre=genre, poster_url= poster_url, wiki_url= wiki_url )
    else :
        return render_template('error.html', message="Failed to load movie data")

app.run

