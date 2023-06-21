class Category:
    categories = []

    @classmethod
    def add(cls, name):
        if name in cls.categories:
            raise ValueError(f'Category {name} already exists.')
        cls.categories.append(name)
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
        if new_name in cls.categories:
            raise ValueError(f'Category {new_name} already exists.')
        if index < len(cls.categories):
            cls.categories[index] = new_name
        else:
            cls.categories.append(new_name)
