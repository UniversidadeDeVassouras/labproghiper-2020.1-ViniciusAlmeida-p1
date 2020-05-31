from application import app
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.categories import Category
from flask import render_template, request
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.video import Videos


@app.route("/category/<int:category_id>")
def category(category_id):
    category = CategoryDAO().search (category_id)
    category_dao = CategoryDAO()
    category_list = category_dao.category_list_categorie()
    return render_template("categories.html", category = category, category_list = category_list)

