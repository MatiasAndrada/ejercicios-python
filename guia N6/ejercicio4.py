# Ingresar un número del 1 al 10 y escribir su correspondiente en letras. 
# Si el número no está entre 1 y 10 escribir “Número fuera de rango”.

numero = int(input("Ingrese un número del 1 al 10: "))

if numero == 1:
    print("Uno")
elif numero == 2:
    print("Dos")
elif numero == 3:
    print("Tres")
elif numero == 4:
    print("Cuatro")
elif numero == 5:
    print("Cinco")
elif numero == 6:
    print("Seis")
elif numero == 7:
    print("Siete")
elif numero == 8:
    print("Ocho")
elif numero == 9:
    print("Nueve")
elif numero == 10:
    print("Diez")
else:
    print("Número fuera de rango")
    