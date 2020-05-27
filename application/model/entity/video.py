class Videos:
    def __init__(self, title, description, thumb, video):
        self._title = title
        self._description = description
        self._thumb = thumb
        self._video = video
        self._commentary = []


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

    def get_video (self):
        return self._video 


    