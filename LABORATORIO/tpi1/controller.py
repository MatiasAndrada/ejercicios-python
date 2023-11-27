import os  # Importacion para tener permisos de escritura y lectura de archivos

dir_raiz = "./data"

# si no existe el directorio, lo crea
if not os.path.isdir(dir_raiz):  # Verificar si el directorio existe
    os.mkdir(dir_raiz)  # Si no existe, crearlo


def saveOrder(name, dni, m3):
    # normalizar datos
    name = str(name.capitalize())  # Capitalizar el nombre
    dni = str(dni)  # str convierte cualquier tipo de dato a string
    m3 = str(m3)
    try:
        # Verificar si el archivo existe
        ifExists = os.path.isfile(f"{dir_raiz}/pedido-{dni}.txt")
        if ifExists:  # Si el archivo existe, imprimir el mensaje, sino, crear el archivo
            # Si el archivo existe, no se puede guardar otro
            print("Usted ya tiene un pedido guardado")
            doc = open(f"data/pedido-{dni}.txt", "r")  # Abrir el archivo
            print(doc.read())  # Leer el archivo
            doc.close()  # Cerrar el archivo
        else:
            # Abrir el archivo en modo append (agregar)
            doc = open(f"data/pedido-{dni}.txt", "a")
            # Escribir en el archivo
            doc.write(f"Nombre: {name}\nDNI: {dni}\nM3: {m3}")
            doc.close()  # Cerrar el archivo
            # Abrir el archivo en modo lectura
            doc = open(f"data/pedido-{dni}.txt", "r")
            print(doc.read())  # Leer el archivo
            doc.close()  # Cerrar el archivo
    except:  # Si hay un error, imprimir el mensaje
        print("Error: Algo salió mal")


def findOrder(dni):
    # normalizar datos
    dni = str(dni)
    try:
        # Verificar si el archivo existe
        ifExists = os.path.isfile(f"{dir_raiz}/pedido-{dni}.txt")
        if ifExists:  # Si el archivo existe, leerlo
            # Abrir el archivo en modo lectura
            doc = open(f"data/pedido-{dni}.txt", "r")
            print(doc.read())  # Leer el archivo
            doc.close()  # Cerrar el archivo
        else:
            return "No se encontró el pedido"  # Si el archivo no existe, imprimir el mensaje
    except:
        print("Error: Algo salió mal")  # Si hay un error, imprimir el mensaje
