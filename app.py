#!/usr/bin/python3
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    image = response["preview"][-2]
    subreddit = response["subreddit"]
    nsfw = response["nsfw"]
    return image, subreddit, nsfw

@app.route("/")
def index():
    meme_pic, subreddit, nsfw = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit, nsfw=nsfw)
