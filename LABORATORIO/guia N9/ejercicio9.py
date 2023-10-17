"""
Escribí un programa que permita al usuario ingresar una cantidad de números positivos
indefinida (la cantidad que ingresará no se conoce y puede cambiar en cada ejecución),
finalizando cuando ingresa el número 0 (que no se tendrá en cuenta). Una vez terminada la
lectura de números, informar cuál fue el mayor de los números ingresados.
"""

mayor = 0 

num = float(input("Ingrese un número: "))

while num != 0:
    if num < 0:
        num = float(input("Ingrese un número válido: "))
    else:
        if num > mayor:
            mayor = num
        num = float(input("Ingrese un número: "))
        
print(f"El mayor número ingresado es {mayor}")