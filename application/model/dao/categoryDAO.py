class CategoryDAO:
    def __init__ (self):
        self._category_list_id = []

    
    def category_list (self):
        return self._category_list_id

    def search (self, id):
        category_list_id = list (filter(lambda categories : categories.get_id() == id, self._category_list_id))
        if len (category_list_id) == 0:
            return None
        return category_list_id