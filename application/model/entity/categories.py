from flask import current_app


class Category:
    def __init__ (self, id, title):
        self._id = id
        self._title = title

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id 

    def get_title (self):
        return self._title

    def get_video_category_id (self):
        videos = current_app.config ['videos']
        videos_category = []
        for i, video in enumerate (videos.get_list_video()):
            if video.get_category_id () == self.get_id():
                videos_category.append (video)
        return videos_category

    





    
