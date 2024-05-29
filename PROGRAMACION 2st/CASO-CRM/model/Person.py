class Person:
    def __init__(self, dni, name, address, genre, telephone):
        self.dni = dni,
        self.name = name,
        self.address = address,
        self.genre = genre,
        self.telephone = telephone

    def __str__(self):
        print(f"dni: {self.dni} \n nombre: {self.name} \n apellido: {self.address} \n genero: {self.genre} \n teléfono: {self.telephone}")

    def isPersonExist(self, dni):
        if dni  == self.dni:
            return True
        else:
            return False