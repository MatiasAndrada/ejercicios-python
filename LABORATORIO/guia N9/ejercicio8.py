"""
Escribí un programa que permita al usuario ingresar los montos de las compras de un
cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. 
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al
finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el monto
total de 1000, se le debe aplicar un 10% de descuento.
"""

monto = 0
discount = 0
venta = float(input("Ingrese el monto de la venta: "))

while venta != 0:
    if venta < 0:
        venta = float(input("Ingrese un monto válido: "))
    else:
        monto += venta
        venta = float(input("Ingrese el monto de la venta: "))

if monto > 1000:
    discount = 10
    
if discount != 0:
    monto -= monto * (discount/100)
    print(f"El monto total a pagar es de ${monto:.2f}")
else:
    print(f"El monto total a pagar es de ${monto:.2f}")