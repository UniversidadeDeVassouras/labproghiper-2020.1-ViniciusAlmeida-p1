from application import app
from flask import render_template
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.categories import Category



@app.route ("/")
def home():
    category_dao = CategoryDAO ()
    category_list = category_dao.category_list_categorie()
    return render_template("home.html", category_list = category_list)

