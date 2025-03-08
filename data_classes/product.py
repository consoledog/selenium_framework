class Product:
    def __init__(self, title: str, price: str, description: str):
        self._title = title
        self._price = price
        self._description = description

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not value.startswith("$"):
            raise ValueError("Price must start with '$'")
        self._price = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    
