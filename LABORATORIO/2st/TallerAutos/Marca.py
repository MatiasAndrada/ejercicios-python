class Marca:
    def __init__(self, cod, nombre):
        self.codigo = cod
        self.nombre = nombre

    def __str__(self):
        return f"{self.codigo}-{self.nombre}"

    def __repr__(self):
        return self.__str__()
