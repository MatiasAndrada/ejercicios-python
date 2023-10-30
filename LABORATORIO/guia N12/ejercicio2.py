# Recorrer un array con num decimales y al finalizar mostrar los siguientes datos:
# - El mayor elemento del array
# - El menor elemento del array
# - El promedio de todos los elementos del array


nElementos = int(input("Ingrese el numero de elementos: "))
nPromedio = 0
array = []

for i in range(nElementos):
    array.append(float(input("Ingrese un numero: ")))

print("Array original: ", array)

# Recorrer el array y comparar cada elemento con el mayor y menor

for i in range(len(array)):
    nMayor = array[0]
    nMenor = array[0]
    if array[i] > nMayor:
        nMayor = array[i]
    if array[i] < nMenor:
        nMenor = array[i]

nPromedio = sum(array) / len(array)

print("El mayor elemento del array es: ", nMayor)
print("El menor elemento del array es: ", nMenor)
print("El promedio de todos los elementos del array es: ", nPromedio)
