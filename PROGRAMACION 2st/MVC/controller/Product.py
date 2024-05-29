from models.Product import Product


class Product():
    def __init__(self, view):
        self.view = view,
        self.ProductList = []

    def cargarDatos(self):
        with open("'data/products") as file:
            file.readLines()
            for i in file:
                self.ProductList.append(Product())
