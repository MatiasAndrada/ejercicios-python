from product import Product

route_file = "./data/productos.txt"
products = []


def uploadProducts():
    with open(route_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            print(name)
            price = float(data[1])
            tipeDolar = int(data[2])
            p = Product(name, price, tipeDolar)
            products.append(p)


def main():
    uploadProducts()
    while True:
        print("Bienvenido al sistema de venta de productos")
        print("Elija la cotización de su preferencia")
        print("1. Dolar")
        print("2. Marca")
        print("3. Oficial")
        res = int(input("Ingrese su elección: "))
        if res in [1, 2, 3]:
            print(f"Se ha guardado su elección: ")
            for p in products:
                print(p)
                print("precio convertido:", p.convertPrice(res))
        else:
            break


if __name__ == "__main__":
    main()
