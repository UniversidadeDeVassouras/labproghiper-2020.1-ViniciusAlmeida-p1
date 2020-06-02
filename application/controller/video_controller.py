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
    

@app.route ("/video/commentary", methods = ['POST'])
def comment ():
    try:
        comments = current_app.config ['comments']
        video = current_app.config ['videos']
        comment = Commentary(request.form['comments'], int(request.form['id_video']))

        comments.add_commentary(comment)
        print (comments)

        return jsonify (comment.__dict__)
    except Exception as e:
        return str(e)
        

@app.route ("/category/<int:category_id>/video/<int:video_id>")
def video (category_id, video_id):
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']
    commentary = current_app.config ['comments']
    commentary_video = commentary.get_commentary_video(video_id)
    category = categories.search(category_id)
    video = videos.get_video_by_id(video_id)
    video.set_qtdVisualization (video.get_qtdVisualization() +1)
    return render_template ("video.html", video = video, commentary = commentary_video)


