class Commentary:
    def __init__ (self, content, author):
        self._content = content
        self._author = author

    def get_content(self):
        return self._content

    def get_author (self):
        return self._author

    