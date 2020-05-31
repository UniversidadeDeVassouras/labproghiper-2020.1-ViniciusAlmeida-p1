from flask import current_app

from application.model.entity.video import Videos
from application.model.entity.categories import Category
from application.model.entity.comments import Commentary


class VideoDAO:
    def __init__(self):
       self._list_video = []
       self._list_video.append (Videos(1, "TESTE JOGOS", "DESCRIÇÃO JOGOS", "/assets/img/testejogos.jpg", "/assets/img/test.mp4", 1))
       self._list_video.append (Videos(2, "TESTE CULINARIA", "DESCRIÇÃO CULINARIA", "/assets/img/testeculinaria.jpg", "/assets/img/test.mp4", 1))
       
    def get_list_video(self):
        return self._list_video

    def get_video_by_id (self, video_id):
        find_video = None
        for i, video in enumerate (self.get_list_video()):
            if video.get_id() == int(video_id):
                find_video = video
        return find_video


