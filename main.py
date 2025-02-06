import flask
from flask import render_template
import random
from movie import tmdb_data, wiki_data, Movie_id_list

app = flask.Flask(__name__)

@app.route("/")
def main():
    movie_id = random.choice(Movie_id_list)
    movie_data = tmdb_data(movie_id)

    if movie_data:
        movie_title = movie_data.get("original_title", "Unknown Title")
        tagline = movie_data.get("tagline", "")
        
        genres = movie_data.get("genres", [])
        genre = ", ".join([g["name"] for g in genres]) if genres else "Unknown Genre"
        
        
        poster_path = movie_data.get("poster_path", "")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""

        wiki_url = wiki_data(movie_title)
        
        return render_template('index.html', title=movie_title, tagline=tagline, genre=genre, poster_url=poster_url, wiki_url=wiki_url)
    else:
        return "Error: Could not fetch movie data", 500  # Return an error message

# Running Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port= os.getenviron("PORT", "8080"))

