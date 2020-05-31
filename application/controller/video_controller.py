from application import app
from flask import render_template, request, current_app, jsonify
from application.model.dao.categoryDAO import CategoryDAO
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.comments import Commentary

@app.route ("/video/like", methods = ["POST"])
def like ():
    try:
        videos = current_app.config ['videos']
        video_id = (request.form["video_id"])
        video = videos.get_video_by_id(video_id)
        video.set_qtdLike (video.get_qtdlike() +1)
        return jsonify(qtd_likes = video.get_qtdlike())
    except Exception as e:
        return str(e)
    


@app.route ("/category/<int:category_id>/video/<int:video_id>")
def video (category_id, video_id):
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']
    category = categories.search(category_id)
    video = videos.get_video_by_id(video_id)
    video.set_qtdVisualization (video.get_qtdVisualization() +1)
    return render_template ("video.html", video = video)


