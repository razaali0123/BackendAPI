from flask import Flask, request, jsonify
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
    recommended = []
    content = request.json
    for id in content['ids']:
        url = "https://api.themoviedb.org/3/movie/" + str(id) + "/recommendations?api_key=a19d7946ea240c2c92f7d5fb6813b3f6&language=en-US&page=1"
        response_post = requests.get(url).json()
        res_post = response_post["results"]
        res_post = res_post[0]
        recommended.append(res_post['title'])
    return jsonify({"Recommend_movies": recommended})
    return response_post




    
