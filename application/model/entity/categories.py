class Category:
    def __init__ (self, description, title, video):
        self._title = description
        self._description = title
        self._video = video

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id 

    def get_description (self):
        return self._description

    def get_title (self):
        return self._title

    def get_video (self):
        return self._video

    
