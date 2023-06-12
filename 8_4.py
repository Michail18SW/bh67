class Category:
    categories = []

    @classmethod
    def add(cls, name, is_published=False):
        for category in cls.categories:
            if category['name'] == name:
                raise ValueError(f'Category {name} already exists.')
            cls.categories.append({'name': name, 'is_published': is_published})
            return len(cls.categories) - 1

    @classmethod
    def get(cls, index):
        try:
            return cls.categories[index]
        except IndexError:
            raise IndexError(f'No category at index {index}')

    @classmethod
    def delete(cls, index):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_name):
        for category in cls.categories:
            if category['name'] == new_name:
                raise ValueError(f'Category {new_name} already exists.')
            if index < len(cls.categories):
                cls.categories[index]['name'] = new_name
            else:
                cls.categories.append({'name': new_name, 'is_published': False})

    @classmethod
    def make_published(cls, index):
        try:
            cls.categories[index]['is_published'] = True
        except IndexError:
            raise IndexError(f'No category at index {index}')

    @classmethod
    def make_unpublished(cls, index):
        try:
            cls.categories[index]['is_published'] = False
        except IndexError:
            raise IndexError(f'No category at index {index}')















