from spotify import Spotify
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)
# app = Flask("app")

playlist = "0m0xz4tyUyhQuJXQEwtyWq"


@app.route("/")
def home():
    return render_template("index.html")
    
    
@app.route("/", methods=["POST"])
def home2():
    client_id = request.form["client_id"]
    client_secret = request.form["client_secret"]
    playlist_id = request.form["playlist_id"]
    spotify = Spotify()
    spotify.get_access_token(client_id, client_secret, playlist_id)
    return render_template("index.html", songs = spotify.my_songs)
# app.add_url_rule("/", view_func=Spotify.test_route, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=3000)