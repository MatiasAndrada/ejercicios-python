# Manejo de excepciones en un input
while True:
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        cociente = dividendo / divisor
        print("El cociente es: ", cociente)
        break
    except ValueError:
        print("Error: El valor ingresado no es un número")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except:
        print("Error: Algo salió mal")
