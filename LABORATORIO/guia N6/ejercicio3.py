# Escribir  un  programa  que  pida  al  usuario  un  número  entero  y  muestre  por  pantalla  si  es  par o impar.
numero = int(input("Ingrese un número entero: "))

#Verificar la paridad del número
if numero % 2 == 0:
    print (f"El número {numero} es par")
else:
    print (f"El número {numero} es impar")