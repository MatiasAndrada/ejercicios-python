import os  # Importacion para tener permisos de escritura y lectura de archivos

dir_raiz = "./data"

# si no existe el directorio, lo crea
if not os.path.isdir(dir_raiz):
    os.mkdir(dir_raiz)


def saveOrder(name, dni, m3):
    # normalizar datos
    name = str(name.capitalize())  # Capitalizar el nombre
    dni = str(dni)  # str convierte cualquier tipo de dato a string
    m3 = str(m3)
    try:
        ifExists = os.path.isfile(f"{dir_raiz}/pedido-{dni}.txt")
        if ifExists:
            print("Usted ya tiene un pedido guardado")
            doc = open(f"data/pedido-{dni}.txt", "r")
            print(doc.read())
            doc.close()
        else:
            doc = open(f"data/pedido-{dni}.txt", "a")
            doc.write(f"Nombre: {name}\nDNI: {dni}\nM3: {m3}")
            doc.close()
            doc = open(f"data/pedido-{dni}.txt", "r")
            print(doc.read())
    except:
        print("Error: Algo salió mal")


def findOrder(dni):
    # normalizar datos
    dni = str(dni)
    try:
        ifExists = os.path.isfile(f"{dir_raiz}/pedido-{dni}.txt")
        if ifExists:
            doc = open(f"data/pedido-{dni}.txt", "r")
            print(doc.read())
            doc.close()
        else:
            return "No se encontró el pedido"
    except:
        print("Error: Algo salió mal")
