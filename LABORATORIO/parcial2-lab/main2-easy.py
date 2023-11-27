cadena = input("Ingrese una cadena de texto: ").lower()

while cadena == "":
    cadena = input(
        "No puede ingresar una cadena vacía, Ingrese una cadena de texto: ").lower()

letra_no_repetida = "_"

for letra in cadena:  # Se recorre la cadena de texto
    if cadena.count(letra) == 1:  # Si la letra se repite una sola vez
        letra_no_repetida = letra  # Se asigna la letra a la variable letra_no_repetida
        break  # Se rompe el ciclo for
print(letra_no_repetida)
