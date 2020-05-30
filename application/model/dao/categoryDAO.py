from application.model.entity.video import Videos
from application.model.entity.categories import Category


class CategoryDAO:
    def __init__ (self):

        self._category_list = []
        self._category_list.append(Category(1, "Jogos", " Jogos"))
        self._category_list.append(Category(2, "Culinária", "Culinaria"))

    def category_list_categorie (self):
        return self._category_list

    def search (self, id):
        category = None
        for index, item in enumerate(self.category_list_categorie()):
            print (item.get_id())
            if item.get_id() == id:
                category = item
                return category
        return category


