class Category:
    def __init__ (self, description, title, video_list, id):
        self._title = description
        self._description = title
        self._video_list = video_list
        self._id = id
        

    def get_description (self):
        return self._description

    def get_title (self):
        return self._title

    def get_video_list (self):
        return self._video_list

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id 

    
