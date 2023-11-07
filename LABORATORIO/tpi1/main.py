"""
Sist de pedidos de hormigón
LUMNOS: MAtIAS ANDRADA, EMILIANO CORONEL
"""

print("Bienvenido al sistema de pedidos de hormigon")

#  operacion a realizar

print("Ingrese la operación que desea realizar: ")
print("1. Generar un pedido")
print("2. Consultar un pedido")

# validar que la operacion ingresada sea correcta
while True:
    try:
        operacion = int(input("Ingrese la operación que desea realizar: "))
        if operacion not in [1, 2]:
            raise ValueError
        break
    except ValueError:
        print("Opcion incorrecta, ingrese nuevamente la operación que desea realizar")


# si la operacion es 1, generar un pedido
if operacion == 1:
    print("Generar un pedido")
    # validar que el sistema de medición ingresado sea correcto
    while True:
        try:
            sist_ingresado = int(
                input("Ingrese el sistema de medición a utilizar: "))
            if sist_ingresado not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print(
                "Opcion incorrecta, ingrese nuevamente el sistema de medición a utilizar")

    # solicitar las dimensiones de la superficie donde se utilizara el hormigón

    print(
        f"Ingrese las dimensiones de la superficie en {sist_ingresado} donde se utilizara el hormigón:")
    # validar quie las dimensiones sean positivas
    largo = 0
    while largo <= 0:
        try:
            largo = float(input("Ingrese el largo (debe ser positivo): "))
            if largo <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    ancho = 0
    while ancho <= 0:
        try:
            ancho = float(input("Ingrese el ancho (debe ser positivo): "))
            if ancho <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    alto = 0
    while alto <= 0:
        try:
            alto = float(input("Ingrese el alto (debe ser positivo): "))
            if alto <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    # normalizar las dimensiones a metros y calcular los metros cubicos de hormigon requeridos
    metros_cubicos = 0
    if sist_ingresado == 1:
        metros_cubicos = largo * ancho * alto
    elif sist_ingresado == 2:
        metros_cubicos = (largo * 0.3048) * (ancho * 0.3048) * (alto * 0.3048)
    elif sist_ingresado == 3:
        metros_cubicos = (largo * 0.01) * (ancho * 0.01) * (alto * 0.01)
    # mostrarle el total de metros cubicos de hormigón requeridos,
    print(
        f"La cantidad de metros cúbicos de hormigón requeridos es: {metros_cubicos} m3")

    # preguntar si desea guardar el pedido, si es un si preguntarle el nombre y  DNI.
    while True:
        try:
            guardar = int(
                input("Desea guardar el pedido?\n1. Si\n2. No\nIngrese la opción: "))
            if guardar not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Opcion incorrecta, ingrese nuevamente la opción")

    if guardar == 1:
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                if nombre == "":
                    raise ValueError
                break
            except ValueError:
                print("El nombre no puede estar vacio")
        while True:
            try:
                dni = int(input("Ingrese el DNI: "))
                if dni >= 0:
                    raise ValueError
                break
            except ValueError:
                print("El DNI debe ser un número positivo")

elif operacion == 2:
    print("Consultar un pedido")
