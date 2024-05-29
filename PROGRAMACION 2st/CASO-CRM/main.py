from model.Person import PersonClass

def main():
    print("Bienvenido al sistema de gestión CMS")

    #1 Autenticarse en el sist - Crear persona(cliente/empleado)
    print("Que operación desea realizar: ")
    print("1. Autenticarse")
    print("2. Registrar")
    while True: 
        try: 
            option = int(input())
            if option not in [1,2]:
                raise ValueError
            break
        except ValueError:
            print("ERROR: El valor ingresado no corresponde a una operación")
        except:
            print("ERROR: Algo salio mal...")
    if option == 1:
        print("opción 1")
    elif option == 2:
        print("Registro")
        dni = input("Ingresar DNI:")

    dni = input("Ingresar DNI:")




if __name__ == '__main__':
    main()
