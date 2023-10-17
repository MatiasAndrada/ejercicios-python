"""
Escribí un programa que, dado un número entero positivo, calcule y muestre su factorial. El
factorial de un número se obtiene multiplicando todos los números enteros positivos que hay
entre el 1 y ese número. El factorial de 0 es 1.

Por ejemplo, si deseas calcular el factorial de 5:

5! (leído como "5 factorial") se calcula así:
5 × 4 × 3 × 2 × 1 = 120
"""

num = int(input("Ingrese un número: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es {factorial}")