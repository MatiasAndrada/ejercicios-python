# Dado un array de N elementos, genere otro sin elementos repetidos.

nElementos = int(input("Ingrese el numero de elementos: "))
array = []

for i in range(nElementos):
    array.append(int(input("Ingrese un numero: ")))

print("Array original: ", array)

array2 = []
array2 = array

for i in range(len(array)):
    for j in range(len(array2)):  # recorre el array2
        if array[i] == array2[j]:  # si el elemento del array es igual al elemento del array2
            array2[j] = array2[j] - 1  # restarle 1


print("Array sin elementos repetidos: ", array2)
