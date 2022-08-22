from flask import Flask
import requests

app = Flask(__name__)




@app.route("/")
def hello():
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=a19d7946ea240c2c92f7d5fb6813b3f6&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate")
    return response.json()