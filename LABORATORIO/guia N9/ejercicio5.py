"""
Escribí un programa que, dado un número por el usuario, muestre todos sus divisores
positivos. Recordá que un divisor es aquel que divide al número de forma exacta (con resto
0).
"""

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        


