from flask import render_template

from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/search/")
def search():
    return render_template("search.html")
