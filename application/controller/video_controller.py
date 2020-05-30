from application import app
from flask import render_template
from application.model.dao.categoryDAO import CategoryDAO
from application.model.dao.videoDAO import videoDAO
from application.model.entity.comments import Commentary

@app.route ("/category/<int:category_id>/video/<int:video_id>")
def video (category_id, video_id)
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']
    comments = current_app.config ['comments']
    category = categories.get_id (category_id)
    videos_categorie = videos.get_id (video_id)
    video.set_qtdVisualization(video.get_qtdVisualization() + 1)
    video_comments = comments.