"""
Sist de pedidos de hormigón
LUMNOS: MAtIAS ANDRADA, EMILIANO CORONEL
"""

# Importacion de funciones del controlador para guardar y buscar pedidos
from controller import saveOrder, findOrder

print("Bienvenido al sistema de pedidos de hormigon")

#  operacion a realizar

print("Ingrese la operación que desea realizar: ")
print("1. Generar un pedido")
print("2. Consultar un pedido")

# validar que la operacion ingresada sea correcta
while True:  # bucle infinito
    try:  # try catch para capturar errores
        # solicitar la operacion
        operacion = int(input("Ingrese la operación que desea realizar: "))
        if operacion not in [1, 2]:  # si la operacion no es 1 o 2, se lanza un error
            raise ValueError
        break  # si no hay errores, se sale del bucle
    except ValueError:  # si hay un error, se imprime el mensaje
        print("Opcion incorrecta, ingrese nuevamente la operación que desea realizar")

# si la operacion es 1, generar un pedido
if operacion == 1:
    print("Generar un pedido")
    # validar que el sistema de medición ingresado sea correcto
    # preguntar por el sistema de medición

    print("Ingrese el sistema de medición que desea utilizar: ")
    print("1. Metros")
    print("2. Pies")
    print("3. Centímetros")
    while True:
        try:
            sist_ingresado = int(
                input(""))
            if sist_ingresado not in [1, 2, 3]:
                raise ValueError
            break

        except ValueError:
            print(
                "Opcion incorrecta, ingrese nuevamente el sistema de medición a utilizar")

        match sist_ingresado:  # switch case. Para poder devolver un valor distinto a la var sin modificarla
            case 1:
                print("Usted eligió metros")
            case 2:
                print("Usted eligió pies")
            case 3:
                print("Usted eligió centímetros")

    # validar quie las medidas sean positivas
    largo = 0
    while largo <= 0:
        try:
            largo = float(input("Ingrese el largo : "))
            if largo <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    ancho = 0
    while ancho <= 0:
        try:
            ancho = float(input("Ingrese el ancho : "))
            if ancho <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    alto = 0
    while alto <= 0:
        try:
            alto = float(input("Ingrese el alto : "))
            if alto <= 0:
                raise ValueError
        except ValueError:
            print("El valor ingresado debe ser un número positivo")

    # normalizar las dimensiones a metros y calcular los metros cubicos de hormigon requeridos
    metros_cubicos = 0
    if sist_ingresado == 1:
        metros_cubicos = largo * ancho * alto
    elif sist_ingresado == 2:
        # convertir pies a metros
        largo = largo * 0.3048
        ancho = ancho * 0.3048
        alto = alto * 0.3048
        # hacer conversion a metros cubicos
        metros_cubicos = largo * ancho * alto
    elif sist_ingresado == 3:
        # convertir centimetros a metros
        largo = largo / 100
        ancho = ancho / 100
        alto = alto / 100
        # hacer conversion a metros cubicos
        metros_cubicos = largo * ancho * alto
    # mostrarle el total de metros cubicos de hormigón requeridos,
    print(
        f"La cantidad de metros cúbicos de hormigón requeridos es: {metros_cubicos} m3")

    # preguntar si desea guardar el pedido, si es un si preguntarle el nombre y  DNI.
    while True:
        print("Desea guardar el pedido?")
        print("1. Si")
        print("2. No")
        try:
            guardar = int(input(""))
            if guardar not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Opcion incorrecta, ingrese nuevamente la opción:")

    if guardar == 1:
        # solicitar el nombre y el DNI
        while True:
            try:
                # solicitar el nombre
                nombre = str(input("Ingrese el nombre: "))
                if nombre == "":
                    raise ValueError  # si el nombre esta vacio, se lanza un error
                break
            except ValueError:
                print("El nombre no puede estar vacio")
        while True:
            try:
                dni = int(input("Ingrese el DNI: "))  # solicitar el DNI
                if dni >= 0:
                    break
            except ValueError:
                print("El DNI debe ser un número positivo")
        # guardar el pedido
        saveOrder(nombre, dni, metros_cubicos)
    elif operacion == 2:
        print("Consultar un pedido")
        while True:
            try:
                # solicitar el DNI
                dni = int(input("Ingrese el DNI: "))
                if dni >= 0:
                    raise ValueError
                # buscar el pedido
                findOrder(dni)
                break
            except ValueError:
                print("El DNI debe ser un número positivo")
