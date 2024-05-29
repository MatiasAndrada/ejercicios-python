class Vehiculo:
    def __init__(self, cod, patente, tipo, marca, modelo, propietario):
        self.codigo = cod
        self.patente = patente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario

    def __str__(self):
        return f"{self.codigo} - {self.patente} - {self.tipo} - {self.marca} - {self.modelo} - {self.propietario}"

    def __repr__(self):
        return {
            "codigo": self.codigo,
            "patente": self.patente,
            "tipo": self.tipo,
            "marca": self.marca,
            "modelo": self.modelo,
            "propietario": self.propietario
        }
