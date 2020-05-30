from flask import current_app


class Category:
    def __init__ (self, id, description, title, video_list):
        self._id = id
        self._title = title
        self._description = description
        self._video_list = video_list
        

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id 

    def get_description (self):
        return self._description

    def get_title (self):
        return self._title

    def get_video_list (self):
        return self._video_list

    def get_video_category_id (self, video_id, list_video_by_category):
        videos = current_app.config ['videos']
        videos_category = []
        for i, video in enumerate (videos.get_videos()):
            if video.get_video_category_id() == self.get_id():
                videos_category.append (video)
        return videos_category
    





    
