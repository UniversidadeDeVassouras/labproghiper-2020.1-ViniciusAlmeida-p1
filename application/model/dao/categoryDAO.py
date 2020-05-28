from application.model.entity.video import Videos
from application.model.entity.categories import Category


class CategoryDAO:
    def __init__ (self):
        video_list_1 = Videos(1, "Title", "Description", "{{url_for('static','filename = 'assets/img/test.mp4')}}")
        video_list_2 = Videos(2, "Title", "Description", "{{url_for('static','filename = 'assets/img/test.mp4')}}")
        self._category_list = []
        self._category_list.append(Category(1, "Jogos", " Jogos", [video_list_1]))
        self._category_list.append(Category(2, "Culinária", "Culinaria", [video_list_2]))

    def category_list_categorie (self):
        return self._category_list

    def search (self, id):
        category = None
        for index, item in enumerate(self.category_list_categorie()):
            print (item.get_id())
            if item.get_id() == id:
                category = item
                print (category.get_title())
                return category
        return category


