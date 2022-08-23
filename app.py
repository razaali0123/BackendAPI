from flask import Flask, request
import requests

app = Flask(__name__)




@app.route("/movies/<num_pages>")
def get_movie_names(num_pages):
    movie_name = []
    movie_id = []
    for page_num in range(int(num_pages)):
        url = "https://api.themoviedb.org/3/discover/movie?api_key=a19d7946ea240c2c92f7d5fb6813b3f6&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+ str(page_num+1) +"&with_watch_monetization_types=flatrate"
        response = requests.get(url).json()
        res = response['results']

        for obj in res:
            if obj['original_language'] == 'en':
                movie_name.append(obj['original_title'])
                movie_id.append(obj['id'])

    return '<br/>'.join([i + " id:" + str(j) for i,j in zip(movie_name, movie_id) ])

@app.route("/movies/recommendation", methods = ['POST'])
def recommendations():
    content = request.json()
    return content
