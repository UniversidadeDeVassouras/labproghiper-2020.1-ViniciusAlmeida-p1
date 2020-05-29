class Videos:
    def __init__(self, id, title, description, thumb, file_video):
        self._title = title
        self._description = description
        self._thumb = thumb
        self._file_video = file_video
        self._commentary = []
        self._id = id


    def set_commentary (self, commentary):
        self._commentary.append (commentary)

    def set_qtdLike (self, qtdLike):
        self._qtdLike = qtdLike
    
    def set_qtdVisualization (self, qtdVisualization):
        self._qtdVisualization = qtdVisualization

    def get_commentary (self):
        return self._commentary
    
    def get_qtdLike (self):
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
    


    