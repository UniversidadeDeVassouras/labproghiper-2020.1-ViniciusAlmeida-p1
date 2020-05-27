from application import app
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.categories import Category
from flask import render_template, request


@app.route("/category/<category_id>")
def category(category_id):
    category = CategoryDAO().search (category_id)
    return render_template("categories.html", category=category)