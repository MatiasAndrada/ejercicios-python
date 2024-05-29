from Vehiculo import Vehiculo
from Marca import Marca
from Modelo import Modelo
from Propietario import Propietario

vehiculos = []
marcas = []
modelos = []
tipos = []
propietarios = []


def cargar_datos():
    with open("data/marcas.txt") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            marcas.append(Marca(partes[0], partes[1]))

    with open("data/modelos.txt") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            modelos.append(Modelo(partes[0], partes[1]))
    with open("data/tipos.txt") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            tipos.append(partes[0], partes[1])
    with open("data/propietarios.txt") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            propietarios.append(Propietario(partes[0], partes[1], partes[2]))
    with open("data/vehiculos.txt") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            vehiculos.append(
                Vehiculo(partes[0], partes[1], partes[2], partes[3], partes[4], partes[5]))


def buscar_i(lista, i):
    return lista[int(i)]


def registrar_auto():
    codigo = len(vehiculos)
    patente = input("Ingrese la patente del auto: ")
    for tipo in tipos:
        print(tipo)
    optionTipo = int(input("Ingrese el tipo de auto: ")) - 1
    tipo = buscar_i(tipos, optionTipo)
    optionMarca = int(input("Ingrese la marca seleccionada: ")) - 1
    marca = buscar_i(marcas, optionMarca)
    for modelo in modelos:
        print(modelo)
    optionModelo = int(input("Ingrese el modelo del auto: ")) - 1
    modelo = buscar_i(modelos, optionModelo)
    nombre = input("Ingrese el nombre del propietario: ")
    telefono = input("Ingrese el telefono del propietario: ")
    vehiculos.append(Vehiculo(codigo, nombre, patente,
                     optionTipo, optionMarca, optionModelo, codigo))
    marcas.append(Marca(codigo, marca))
    modelos.append(Modelo(codigo, modelo))
    propietarios.append(Propietario(codigo, nombre, telefono))


def listar_autos_propietarios():
    for vehiculo in vehiculos:
        # Next lo que hace es buscar el primer elemento que cumpla con la condición
        marca = next((m for m in marcas if m.codigo == vehiculo.marca))
        modelo = next((m for m in modelos if m.codigo == vehiculo.modelo))
        propietario = next(
            (p for p in propietarios if p.codigo == vehiculo.propietario))

        if marca and modelo and propietario:
            print(f"Vehículo: {vehiculo}")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo}")
            print(f"Propietario: {propietario}")
        else:
            print(f"Información incompleta para el vehículo con código {
                  vehiculo.codigo}")


def cantidad_autos_por_marca():
    for marca in marcas:
        print(marca)
    option = int(input("Ingrese la marca seleccionada: ")) - 1
    marcaSelected = marcas[option]
    cantidad = 0
    for marca in marcas:
        if marca == marcaSelected:
            cantidad += 1
    print(f"La cantidad de autos de la marca {marcaSelected} es {cantidad}")


def cantidad_autos_por_tipo():
    for tipo in tipos:
        print(tipo)
    option = int(input("Ingrese el tipo seleccionado: ")) - 1
    tipoSelected = tipos[option]
    cantidad = 0
    for tipo in tipos:
        if tipo == tipoSelected:
            cantidad += 1
    print(f"La cantidad de autos del tipo {tipoSelected} es {cantidad}")


def main():
    cargar_datos()
    while True:
        print("1. Registrar auto")
        print("2. Listar autos y propietarios")
        print("3. Cantidad de autos por marca")
        print("4. Cantidad de autos por tipo")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_auto()
        elif opcion == "2":
            listar_autos_propietarios()
        elif opcion == "3":
            cantidad_autos_por_marca()
        elif opcion == "4":
            cantidad_autos_por_tipo()
        elif opcion == "5":
            break


if __name__ == '__main__':
    main()
