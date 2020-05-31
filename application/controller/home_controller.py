from application import app
from flask import render_template
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.categories import Category
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.video import Videos



@app.route ("/")
def home():
    category_dao = CategoryDAO ()
    category_list = category_dao.category_list_categorie()
    videodao = VideoDAO ()
    video_list_id = videodao.get_list_video()
    return render_template("home.html", category_list = category_list )


