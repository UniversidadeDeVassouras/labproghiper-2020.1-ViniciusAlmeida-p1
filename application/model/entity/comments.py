from flask import current_app

class Commentary:
    def __init__ (self, content, author, video_id):
        self._content = content
        self._author = author
        self._video_id = video_id

    def get_content(self):
        return self._content

    def get_author (self):
        return self._author

    def get_video_commentary_id (self):
        return self._video_id

    