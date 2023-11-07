# Pedir num de 1 a 10 y guardar fichero tabla-num.txt con la tabla de multiplicar de ese num

import os


def saveTable(num):
    try:
        ifExists = os.path.isfile(f"data/tabla-{num}.txt")
        if ifExists:
            doc = open(f"data/tabla-{num}.txt", "r")
            print(doc.read())
            doc.close()
        else:
            for i in range(1, 11):
                tabla = open(f"data/tabla-{num}.txt", "a")
                tabla.write(f"{num} x {i} = {num * i}\n")
                tabla.close()
            doc = open(f"data/tabla-{num}.txt", "r")
            print(doc.read())
    except:
        print("Error: Algo salió mal")


while True:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        if num < 1 or num > 10:
            raise ValueError
        saveTable(num)
        break
    except ValueError:
        print("Error: El valor ingresado no es un número del 1 al 10")
    except:
        print("Error: Algo salió mal")
