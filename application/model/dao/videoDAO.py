from application.model.entity.video import Videos
from application.model.entity.comments import Commentary
from application.model.entity.categories import Category

class videoDAO:
   def __init__(self):
       self._list_video = []
       self._list_video.append (Videos(1, "Title", "Description", "/assets/img/testejogos.jpg", "/assets/img/test.mp4"))
       self._list_video.append (Videos(2, "Title", "Description", "/assets/img/testeculinaria.jpg", "/assets/img/test.mp4"))

    def get_videos(self):
        return self._list_video
