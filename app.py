from flask import Flask, request, render_template
from random import choice, sample
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

@app.route('/')
def home():
    """homepage"""
    return render_template("home.html")

@app.route('/form')
def form():
    """show form for story inputs"""
    return render_template("form.html")

@app.route('/story')
def story():
    """show completed story with user inputs"""
    wants = request.args.get("comps")

    if wants:
        add_words = sample(COMPLIMENTS, 1)

    v = request.args["verb"]
    n = request.args["noun"]
    return render_template("story.html", verb=v, noun=n, comps=add_words)

