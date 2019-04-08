from flask import Flask, render_template, request
import requests as apirequest
import json



app = Flask(__name__)

@app.route("/")
def index():
    movies = []
    if request.args.get("search") is not None:
        search = request.args.get("search")
    #else:
        # search = "star wars"
        #return render_template("error.html")
        # response = apirequest.get("http://www.omdbapi.com/?apikey=39907301&s=batman")
        response = apirequest.get("http://www.omdbapi.com/?apikey=39907301&s=%s" % search)
        data = response.json()
        movies = data["Search"]
        return render_template("index 2.html", movies=movies)
#else:
        #return "hi"

#@app.route("/<movie_name>")
#def display_movie_data(movie_name):





if __name__ == "__main__":
    app.run(debug=True)
