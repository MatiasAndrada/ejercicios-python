# Escribir  un  programa  que  pida  al  usuario  dos  números  y  muestre  por  pantalla  su  división.  Si el divisor es cero el programa debe mostrar un error

dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))
if divisor == 0:
    print ("Error: el divisor no puede ser cero")
else:
    print (f"El resultado de la división es {dividendo/divisor:.2f}")
    