"""
Sist de pedidos 

REQUISITOS:
●     Recibir   las   dimensiones   de   la   superficie   donde   se   utilizará   el   hormigón,   ya  sea  en 
 forma de longitud, anchura y altura, o a través de otros parámetros relevantes. 
 ●   Calcular   de   manera   precisa   la   cantidad   de  metros  cúbicos  de  hormigón  requeridos 
 según las dimensiones proporcionadas y otros factores relevantes. 
 ●   Presentar  los  resultados  de  manera  clara  y  comprensible  para  el  cliente,  mostrando 
 tanto   la   cantidad   de   hormigón   requerida   como   posiblemente   otros   detalles 
 importantes. 
 ●   Proporcionar  una  interfaz  amigable  e  intuitiva  que  guíe  al  cliente  a  través  del  proceso 
 de ingreso de datos y obtención de resultados. 
 ●   Ser   capaz   de   manejar   diferentes   unidades   de   medida,   como   metros,   pies, 
 centímetros, etc., para adaptarse a las preferencias de los clientes. 
 ●   Registrar   el   pedido   del   cliente   en   un   archivo   de   control   para   la  empresa  donde  se 
 deberá visualizar el cliente y los metros solicitados. 
 ●   Proporcionar   un   archivo   que   podrá  ser  impreso  para  entregárselo  al  cliente  con  los 
 datos   ofrecidos,   el   cálculo   realizado   y   el   total   de   metros  de  hormigón  que  le  serán 
 entregado 

DISEÑO DEL ALGORITMO:
ENTRADA: dimension de la superficie en forma de longitud, anchura y altura o otros parámetros relevantes
PROCESO:  calcular cantidad de metros cúbicos de hormigón  requeridos.
SALIDA: cantidad de hormigon requerida y otros detalles importantes.

ALUMNOS: MAtIAS ANDRADA, EMILIANO CORONEL
"""

print("Bienvenido al sistema de pedidos de hormigon")

# preguntar por el sistema de medición

print("Ingrese el sistema de medición que desea utilizar: ")
print("1. Metros")
print("2. Pies")
print("3. Centímetros")
sist_ingresado = int(input("Ingrese el sist de medición a utilizar: "))

match sist_ingresado:
    case 1:
        sist_ingresado = "metros"
    case 2:
        sist_ingresado = "pies"
    case 3:
        sist_ingresado = "centímetros"
    case _:
        print("Opcion incorrecta, ingrese nuevamente el sistema de medición")
        sist_ingresado = int(input("Ingrese el sist de medición a utilizar: "))

print(
    f"Ingrese las dimensiones de la superficie en {sist_ingresado} donde se utilizara el hormigón:")

largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))
alto = float(input("Ingrese el alto: "))

# calcular cantidad de metros cúbicos de hormigón requeridos
metros_cubicos = 0
if sist_ingresado == "metros":
    metros_cubicos = largo * ancho * alto
elif sist_ingresado == "pies":
    metros_cubicos = (largo * 0.3048) * (ancho * 0.3048) * (alto * 0.3048)
elif sist_ingresado == "centímetros":
    metros_cubicos = (largo * 0.01) * (ancho * 0.01) * (alto * 0.01)
    print(
        f"La cantidad de metros cúbicos de hormigón requeridos es: {metros_cubicos} m3")

# preguntar si desea guardar el pedido, si es un si preguntarle el nombre y mostrarle el total de metros cubicos de hormigón requeridos
print("Desea guardar el pedido?")
print("1. Si")
print("2. No")
guardar = int(input("Ingrese la opción: "))
if guardar == 1:
    nombre = input("Ingrese el nombre del cliente: ")
    print(f"El cliente {nombre} solicito {metros_cubicos} m3 de hormigón")
else:
    print("Gracias por utilizar el sistema de pedidos de hormigón")
