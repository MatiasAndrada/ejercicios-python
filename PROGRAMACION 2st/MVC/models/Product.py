

class Product():
    def __init__(self, c, n, p):
        self.cod = c,
        self.name = n
        self.price = p

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.cod, self.name, self.price
