#! Tenrer en cuenta que es una buena practica usar una normalizacion de los datos para de que no halla un error con su valor en el codigo ASCII por que su valor cambia dependiendo el si es mmayuscula o minuscula


#Pedir al usuario que ingrese una letra y hacer un condicional para devolverle el grupo que pertenece separando el abecedario en 2 
print("PROGRAMA 1")
letra = input("Ingrese una letra: ")

if letra in "abcdefghijklmnñopqrstuvwxyz":
    if letra in "abcdefghijklmn":
        print("La letra ingresada pertenece al grupo A")
    else:
        print("La letra ingresada pertenece al grupo B")
else:

    print("La letra ingresada no pertenece al abecedario")
    
#hacer lo mismo pero en lugar de usar in usar >= y <= teniendo en cuenta su valor en la tabla ASCII

print("PROGRAMA 2")
letra = input("Ingrese una letra: ")

if letra >= "a" and letra <= "n":
    print("La letra ingresada pertenece al grupo A")
elif letra >= "o" and letra <= "z":
    print("La letra ingresada pertenece al grupo B")
    