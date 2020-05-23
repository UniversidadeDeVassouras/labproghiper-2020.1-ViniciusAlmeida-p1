from application import app
from flask import render_template



@app.route ("/")
def home():
    return render_template("home.html")


@app.route ("/categories")
def categories():
    return render_template("categories.html")

@app.route ("/categories/games")
def games():
    return render_template("jogos.html")

@app.route ("/categories/culinary")
def culinary():
    return render_template("culinaria.html")