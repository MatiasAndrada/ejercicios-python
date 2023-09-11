
# *Ahora quiero hacer la misma función pero con validación en los datos de entrada y que funcione como un programa

from datetime import date
from datetime import timedelta

# def variable global
contadorTickets = 0

def generarTicket(fecha, hora, cancha, telefono, correo):
    # Aumentar el contador de tickets
    global contadorTickets
    contadorTickets += 1
    # Generar el ticket
    ticket = f"""
    Fecha: {fecha}
    Hora: {hora}
    Ticket: {contadorTickets}
    Cancha: {cancha}
    Telefono: {telefono}
    Correo: {correo}
    """
    # Retornar el ticket
    return ticket

def semanaSiguiente():
    #Devuelve en consola cada dia de la semana siguiente a la fecha actual
    for i in range(7):
        print(f"""{i}-{date.today() + timedelta(days=i)}""")
    


print("BIenvenido al sistema de tickets")
print("Que desea realizar?")
print("1- Generar un turno")
print("2- Consultar un turno")
print("3- Salir")

# input de entero
selectMenu = input("Ingrese una opción: ")
while not selectMenu.isdigit():
    print("Ingrese una opción válida")
    selectMenu = input("Ingrese una opción: ")
    
# convertir a entero
selectMenu = int(selectMenu)
if selectMenu == 1:
    print("Ingrese los datos del turno a generar")
    print("Seleccione la fecha:")
    ##Mostrar 1 sem en adelante al dia de hoy
    semanaSiguiente()
    