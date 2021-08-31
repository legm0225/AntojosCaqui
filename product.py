class Product:
    def __init__(self, name, desc, price):
        self.__name = name
        self.__desc = desc
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc):
        self.__desc = desc

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.price

    def __str__(self):
        return f'Product([${self.__price}] {self.__name}: {self.__desc})'


if __name__ == '__main__':
    p = Product('Globe 2', 'Is a colorful group globes', 500)
    print(p)
