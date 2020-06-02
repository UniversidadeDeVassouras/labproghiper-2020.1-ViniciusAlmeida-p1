from flask import current_app

class Videos:
    def __init__(self, id, title, description, thumb, file_video, category_id):
        self._title = title
        self._description = description
        self._thumb = thumb
        self._file_video = file_video
        self._id = id
        self._qtdLike = 0
        self._qtdVisualization = 0
        self._category_id = category_id

    def set_qtdLike (self, qtdLike):
        self._qtdLike = qtdLike
    
    def set_qtdVisualization (self, qtdVisualization):
        self._qtdVisualization = qtdVisualization
    
    def get_qtdlike (self):
        return self._qtdLike

    def get_qtdVisualization (self):
        return self._qtdVisualization

    def get_title (self):
        return self._title
    
    def get_description (self):
        return self._description 

    def get_thumb (self):
        return self._thumb

    def get_file_video (self):
        return self._file_video

    def get_id (self):
        return self._id
    
    def get_category_id (self):
        return self._category_id

    