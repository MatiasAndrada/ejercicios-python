#Crear fn que acepte un array con números  y devuelva el promedio

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

print("Cuantos números desea ingresar?")
cantidad = int(input("Ingrese la cantidad: "))
lista = []
for i in range(cantidad):
    lista.append(int(input(f"Ingrese el numero {i+1}: ")))
print(f"El promedio de los números ingresados es: {promedio(lista)}")


#document a range method
#range(1, 10, 2)
#Default one is 0, and the step is 1.
#First parameter is the start, second is the stop, and the third is the step.
