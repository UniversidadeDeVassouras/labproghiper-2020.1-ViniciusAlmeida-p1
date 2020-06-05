from flask import current_app

from application.model.entity.video import Videos
from application.model.entity.categories import Category
from application.model.entity.comments import Commentary


class VideoDAO:
    def __init__(self):
       self._list_video = []
       self._list_video.append (Videos(1, "Barbarian CoC", "Ataque de Barbaros no Clash of Clans", "/assets/img/barbarian.png", "/assets/img/barbarianvideo.mp4", 1, "03/06/2020"))
       self._list_video.append (Videos(2, "Archer Cosplay", "Cosplay Archer de CoC Real Life", "/assets/img/archer.png", "/assets/img/archervideo.mp4", 1, "28/05/2020"))
       self._list_video.append (Videos(3, "Comida Japonesa", "Aprensentando Rodizio Comida Japonesa", "/assets/img/chefe.png", "/assets/img/comidajaponesa.mp4", 2, "01/06/2020"))
       self._list_video.append (Videos(4, "Macarronada", "Receita de macarrao á carbonara", "/assets/img/chefe01.png", "/assets/img/receitamacarrao.mp4", 2, "04/06/2020"))
       
    def get_list_video(self):
        return self._list_video

    def get_video_by_id (self, video_id):
        find_video = None
        for i, video in enumerate (self.get_list_video()):
            if video.get_id() == int(video_id):
                find_video = video
        return find_video

    def get_video_mais_curtidos (self):
        video = current_app.config ['videos']
        video_mais_curtido = sorted(video.get_list_video(), key=lambda i: i.get_qtdlike(), reverse=True)
        return video_mais_curtido


    def get_video_by_title (self, video_title):
        find_video_title = []
        for i, video in enumerate (self.get_list_video()):
            if video_title.lower() in video.get_title().lower():
                find_video_title.append(video.__dict__)
        return find_video_title

    