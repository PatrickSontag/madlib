# from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
# from random import choice, sample
# from stories import story

# app = Flask(__name__)

# app.config['SECRET_KEY'] = "secret"
# debug = DebugToolbarExtension(app)


# # @app.route('/')
# # def home():
# #     """homepage"""
# #     return render_template("home.html")

# @app.route('/')
# def form():
#     """show form for story inputs"""
#     prompts = story.prompts

#     return render_template("form.html", prompts=prompts)

# @app.route('/story')
# def story():
#     """show completed story with user inputs"""
#     # wants = request.args.get("comps")

#     # if wants:
#     #     add_words = sample(COMPLIMENTS, 1)

#     v = request.args["verb"]
#     n = request.args["noun"]
#     a = request.args["adjective"]
#     n2 = request.args['noun2']

#     ans = { "vb": v,
#             "nou": n,
#             "adj": a,
#             "nou2": n2}

#     return render_template("story.html", verb=v, noun=n, adjective=a, noun2=n2, answers=ans)

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("form.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
