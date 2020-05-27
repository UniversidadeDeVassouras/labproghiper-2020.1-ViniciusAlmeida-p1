from application.model.entity.video import Videos
from application.model.entity.categories import Category


class CategoryDAO:
    def __init__ (self):
        video_list_1 = Videos(1, "Title", "Description", "{{url_for('static','filename = 'assets/img/test.mp4')}}")
        video_list_2 = Videos(2, "Title", "Description", "{{url_for('static','filename = 'assets/img/test.mp4')}}")
        self._category_list = []
        self._category_list.append(Category(1, "Jogos", "Teste jogos", [video_list_1]))
        self._category_list.append(Category(2, "Culinária", "Teste Culinaria", [video_list_2]))

    def category_list_categorie (self):
        return self._category_list

    def search (self, id):
        for i in range (0, len(self._category_list)):
            if self._category_list [i].get_id() == int(id):
                return self._category_list [i]
        return None


