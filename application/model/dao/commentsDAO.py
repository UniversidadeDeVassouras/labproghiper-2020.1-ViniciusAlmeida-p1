from flask import current_app
from application.model.entity.comments import Commentary
from application.model.entity.video import Videos
from application.model.dao.videoDAO import VideoDAO

class CommentaryDAO:
    def __init__ (self):
        self._comments = []
        self._generate_id = 1


    def get_commentary (self):
        return self._comments

    def add_commentary (self, commentary):
        self._comments.append (commentary)


    def get_commentary_video (self, video_id):
        video = current_app.config ['videos']
        commentary = current_app.config ['comments']
        commentary_video = []
        for i, comment in enumerate (commentary.get_commentary()):
            if comment.get_video_commentary_id() == video_id:
                commentary_video.append(comment)
        return commentary_video


    def delete_commentary_by_id(self, comment_id):
        commentary = current_app.config['comments']
        for i, comment in enumerate(commentary.get_commentary()):
            if comment.get_id() == comment_id:
                self._comments.pop(i)
                return comment
        return None


    def set_generate_id (self, generate_id):
        self._generate_id = generate_id


    def get_generate_id (self):
        return self._generate_id