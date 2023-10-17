"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

contraseña = "contraseña"


while True:
    ingreso = input("Ingrese la contraseña: ")
    if ingreso == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        continue
    
    
    