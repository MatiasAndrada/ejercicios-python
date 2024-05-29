# props; codProduct,name,price,tipeDolar
class Product:
    def __init__(self, name, price, tipeDolar):
        self.name = name
        self.price = price
        self.tipeDolar = tipeDolar

    def convertPrice(self, tipeDolar):
        print(self.price)
        if tipeDolar == 1:
            return f"Dolar Blue: ${self.price * 1.6}"
        elif tipeDolar == 2:
            return f"Dolar Marca: ${self.price * 1.4}"
        elif tipeDolar == 3:
            return f"Dolar Oficial: ${self.price * 1.2}"

    def __str__(self):
        return f"Nombre: {self.name} Precio: {self.price} Tipo Dolar: {self.tipeDolar}"

    def __repr__(self):
        return f"Nombre: {self.name} Precio: {self.price} Tipo Dolar: {self.tipeDolar}"
