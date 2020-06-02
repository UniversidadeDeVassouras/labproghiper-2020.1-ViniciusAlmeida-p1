from flask import current_app

class Commentary:
    def __init__ (self, content, video_id):
        self._content = content
        self._video_id = video_id

    def get_content(self):
        return self._content

    def get_video_commentary_id (self):
        return self._video_id

    