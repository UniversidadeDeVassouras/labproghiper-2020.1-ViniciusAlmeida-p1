from application import app
from flask import render_template, current_app
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.categories import Category
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.video import Videos



@app.route ("/")
def home():
    category_dao = current_app.config ['categories']
    videos = current_app.config ['videos']
    category_list = category_dao.category_list_categorie()
    videos_mais_curtidos = videos.get_video_mais_curtidos()
    
    
    return render_template("home.html", category_list = category_list, videos_curtidos = videos_mais_curtidos)


