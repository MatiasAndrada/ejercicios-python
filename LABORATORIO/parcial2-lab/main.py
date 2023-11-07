"""
Solicitar al usuario una cadena de texto aleatoria.
Asegurarse de que este compuesta por minúsculas.

Luego hallar el primer carácter que no repite en la cadena y devolverlo,
Si no existe, mostrar "_"

ALUMNO: Matías Andrada.

"""


def primera_letra_no_repetida_en_cadena(cadena):
    # convertir a minúsculas
    cadena = cadena.lower()
    # crear una lista con cada carácter de la cadena, en la posición que le corresponde
    lista_de_letras = []
    for i in cadena:
        lista_de_letras.append(i)

    # recorrer la lista creada
    for i in lista_de_letras:
        # el método .count(i) devuelve cuantas veces se repite el carácter i en la lista
        if lista_de_letras.count(i) == 1:
            # si el carácter se repite una sola vez, es el primero que no se repite
            print(i)
            break
    else:
        print("_")


# entrada de datos y validación
# INPUT STRING
cadena = str(input("Ingrese una cadena de texto: "))
while cadena == "":
    cadena = str(
        input("No puede ingresar una cadena vacía, Ingrese una cadena de texto: "))

primera_letra_no_repetida_en_cadena(cadena)
