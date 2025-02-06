The Movie Explorer (Deployed APP URL:https://finalproject-922122509110.us-east1.run.app )

Overview

The Movie Explorer is a simple web app that allows users to discover movies by randomly selecting one from a predefined list. The app retrieves movie details from TheMovieDatabase (TMDB) API and displays key information, including the movie title, tagline, genres, and poster image. Additionally, a dynamically generated link takes users to the movie's Wikipedia page, which is fetched via the Wikipedia API.

Technologies Used

The project is built using the following technologies:

Flask: A lightweight Python web framework used to serve the application.

Git + GitHub: Version control for managing code updates and collaboration.

Google Cloud Run: A cloud service for deploying and running the web application.

TMDB API: Provides movie-related data, including details, images, and genres.

Wikipedia API: Retrieves Wikipedia page URLs for the selected movie.

HTML & CSS: Used for structuring and styling the web app to create a user-friendly interface.

Setup Instructions

Prerequisites

Before running the application, ensure you have the following installed:

Python 3

Flask (pip install flask)

Git for version control

A TMDB API key (you can obtain one by creating an account on TMDB)

A Google Cloud account and CLI installed (for deployment)

Installation

Follow these steps to set up the project:

Clone the Repository:

git clone https://github.com/cs540-s25/project1-uagraw7.git
cd project1-uagraw7

Create a Virtual Environment:
Setting up a virtual environment helps manage dependencies effectively.

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install Dependencies:
Install the required libraries by running:

pip install -r requirements.txt

Set Up API Key:
Create a .env file in the project directory and add the following:

TMDB_API_KEY="your_tmdb_api_key"

If deploying on Google Cloud, configure this as an environment variable in Cloud Run.

Run the App Locally:
Start the Flask application with:

flask run

The app should be accessible at http://127.0.0.1:5000/ in your web browser.

Deploying on Google Cloud Run

To make your app accessible online, follow these deployment steps:

Authenticate with Google Cloud:

gcloud auth login
gcloud config set project <project-id>

Build and Deploy:

gcloud builds submit --tag gcr.io/<project-id>/movie-app
gcloud run deploy movie-app --image gcr.io/<project-id>/movie-app --platform managed

After deployment, you will receive a URL where your app is live.

API Usage

TMDB API

The TMDB API is used to fetch details about movies. Key API endpoints include:

Get Movie Details:

https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY

Get Configuration for Image Base URL:

https://api.themoviedb.org/3/configuration?api_key=YOUR_API_KEY

Wikipedia API

The Wikipedia API is used to retrieve the Wikipedia page URL for a given movie title:

Fetch Wikipedia Page Info:

https://en.wikipedia.org/w/api.php?action=query&format=json&titles={movie_title}&prop=info&inprop=url

Error Handling

If the TMDB API request fails, a user-friendly message will be displayed, and a dummy movie entry may be used instead.

If the Wikipedia API request fails, the link will redirect users to the main Wikipedia homepage instead of a specific movie page.
