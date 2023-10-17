"""
El banco Nación le solicita a ud, como programador, crear un algoritmo para un cajero
automático que permita calcular que billetes y cantidades debe entregar cuando se realiza
una extracción de efectivo. Se debe tener en cuenta que el cajero debe entregar la mínima
cantidad de billetes posibles, y la solicitud de dinero no puede ser menor a $1000. Además,
el cajero no puede entregar importes mayores a $50.000, ni más de 60 billetes. Los billetes
con los que cuenta la máquina son: $10, $20, $50, $100, $200, $500 y $1000
"""
monto_a_extraer = int(input("Ingrese el monto a extraer: "))
contador_de_billetes = 0
billetes_de_1000 = 0
billetes_de_500 = 0
billetes_de_200 = 0
billetes_de_100 = 0
billetes_de_50 = 0
billetes_de_20 = 0
billetes_de_10 = 0

if monto_a_extraer < 1000:
    print("El monto ingresado es menor a $1000")
elif monto_a_extraer > 50000:
    print("El monto ingresado es mayor a $50000")
else:
    while monto_a_extraer > 0:
        if contador_de_billetes > 60:
            print("No se puede extraer más de 60 billetes")
            break
        if monto_a_extraer >= 1000:
            billetes_de_1000 = monto_a_extraer // 1000
            if billetes_de_1000 > 0:
                contador_de_billetes += billetes_de_1000
                monto_a_extraer -= billetes_de_1000 * 1000
        elif monto_a_extraer >= 500:
            billetes_de_500 = monto_a_extraer // 500
            if billetes_de_500 > 0:
                contador_de_billetes += billetes_de_500
                monto_a_extraer -= billetes_de_500 * 500
        elif monto_a_extraer >= 200:
            billetes_de_200 = monto_a_extraer // 200
            if billetes_de_200 > 0:
                contador_de_billetes += billetes_de_200
                monto_a_extraer -= billetes_de_200 * 200
        elif monto_a_extraer >= 100:
            billetes_de_100 = monto_a_extraer // 100
            if billetes_de_100 > 0:
                contador_de_billetes += billetes_de_100
                monto_a_extraer -= billetes_de_100 * 100
        elif monto_a_extraer >= 50:
            billetes_de_50 = monto_a_extraer // 50
            if billetes_de_50 > 0:
                contador_de_billetes += billetes_de_50
                monto_a_extraer -= billetes_de_50 * 50
        elif monto_a_extraer >= 20:
            billetes_de_20 = monto_a_extraer // 20
            if billetes_de_20 > 0:
                contador_de_billetes += billetes_de_20
                monto_a_extraer -= billetes_de_20 * 20
        elif monto_a_extraer >= 10:
            billetes_de_10 = monto_a_extraer // 10
            if billetes_de_10 > 0:
                contador_de_billetes += billetes_de_10
                monto_a_extraer -= billetes_de_10 * 10
        else:
            print("No se pueden entregar billetes de menor denominación de $10")
            print(f"Su saldo restante es de ${monto_a_extraer}")
            break
print(f"Se entregarán {contador_de_billetes} billetes de $1000, {billetes_de_500} billetes de $500, {billetes_de_200} billetes de $200, {billetes_de_100} billetes de $100, {billetes_de_50} billetes de $50, {billetes_de_20} billetes de $20 y {billetes_de_10} billetes de $10")
