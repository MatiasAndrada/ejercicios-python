# Definición de la clase
class Libro:
    # Método CONSTRUCTOR de la clase
    def __init__(self, AreaALaQuePertenece, autor, fecha, genero, estado):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.genero = genero
        self.estado = estado
# Métodos de la clase
    # Método __str__
    # Usado para retornar todas propiedades del objeto

    def __str__(self):
        print(f"Nombre: {self.titulo} \n Autor: {self.autor} \n Fecha: {
            self.fecha} \n Genero: {self.genero} \n Estado: {self.estado}")

    def getTitulo(self):
        return self.Titulo

    def getAutor(self):
        return self.Autor

    def getFecha(self):
        return self.fecha

    def getGenero(self):
        return self.genero

    def getEstado(self):
        return self.estado

    def setTitulo(self, titulo):
        if type(titulo) == str:
            self.titulo = titulo
        else:
            print("ERROR")
