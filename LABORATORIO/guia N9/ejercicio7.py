"""
Escribí un programa que permita al usuario ingresar 6 números enteros, que pueden ser
positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el
promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es
necesario evitar que el programa arroje un error si no se ingresaron números positivos.
"""

suma_negativos = 0
prom_positivos = 0
contador_positivos = 0

for i in range(6):
    num = int(input("Ingrese un número: "))
    if num < 0:
        suma_negativos += num
    else:
        contador_positivos += 1
        prom_positivos += num

if contador_positivos != 0:
    prom_positivos /= contador_positivos
    print(f"La sumatoria de los números negativos es {suma_negativos} y el promedio de los positivos es {prom_positivos}, fueron {contador_positivos} números positivos ingresados")
else:
    print(f"La sumatoria de los números negativos es {suma_negativos} y no se ingresaron números positivos")