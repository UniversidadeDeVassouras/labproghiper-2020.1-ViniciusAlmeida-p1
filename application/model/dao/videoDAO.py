class videoDAO:
   def __init__(self):
       self._list_video = []

    def qtd_max_like (self):
        qtd_max_like = self._list_video [0]
        for video in self._list_video:
            if self._qtd_max_like.get_qtdLike > video.get_qtdLike():
                qtd_max_like = video

    def add_view (self, video):
        visualization = video.set_qtdVisualization()
        visualization += 1
        video.set_qtdVisualization(visualization)

    def add_like (self, video):
        qtdLikes = video.set_qtdVisualization()
        qtdLikes += 1
        video.set_qtdVisualization(qtdLikes)

