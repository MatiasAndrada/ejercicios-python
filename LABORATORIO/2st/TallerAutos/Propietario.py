class Propietario:
    def __init__(self, cod, nombre, telefono):
        self.codigo = cod
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.telefono}"

    def __repr__(self):
        return self.__str__()
