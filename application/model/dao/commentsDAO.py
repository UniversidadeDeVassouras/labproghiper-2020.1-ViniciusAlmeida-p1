class CommentaryDAO:
    def __init__ (self):
        self._comments []
        self._comments.append (Commentary("Teste comentario", "Vinicius", 1))
        self._comments.append (Commentary("Teste comentario 2", "Lindomar", 1))


    def get_commentary (self):
        return self._comments

    def add_commentary (self, commentary):
        self._comments.append (commentary)


    def get_commentary_video (self, video_id):
        commentary = current.app_config ['comments']
        commentary_video = []
        for i, comment in enumerate (commentary.get_commentary()):
            if comment.get_video_commentary_id() == video_id:
                commentary_video.append(comment)
        return commentary_video    