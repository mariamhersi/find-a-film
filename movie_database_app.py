from flask import Flask, render_template, request
import requests as apirequest
import json



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index 2.html")

@app.route("/MoviesGenerator")
def index_new():
     return render_template("MoviesGenerator.html")

@app.route("/display_movies", methods=["POST"])
def display_movies():
    movies = []
    form_data = request.form
    movie_name = form_data["search"]
    if movie_name is not None:
    #else:
        # search = "star wars"
        #return render_template("error.html")
        # response = apirequest.get("http://www.omdbapi.com/?apikey=39907301&s=batman")
        response = apirequest.get("http://www.omdbapi.com/?apikey=39907301&s=%s" % movie_name)
        data = response.json()
        movies = data["Search"]
        return render_template("index.html", movies=movies)
    else:
        return form_data["search"]
#else:
        #return "hi"

#@app.route("/<movie_name>")
#def display_movie_data(movie_name):




if __name__ == "__main__":
    app.run(debug=True)
