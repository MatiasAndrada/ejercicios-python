#preguntar prdt a actualizar, precio base y porcentaje de aumento
#descartar decimales y realizar un redondeo particular, todo los precios terminan en 9 o 99
#dependiendo si sus dos últimos dígitos son menores a 50 termina en 9 sino en 99


def porcentajeX(porcentaje, valor):
    aumento = valor * (porcentaje/100)
    new_price = valor + aumento
    new_price = int(new_price)
    return redondeo(new_price)
 
def redondeo(valor):
    if valor % 100 < 50:
        valor = valor - (valor % 100) + 49
    else:
        valor = valor - (valor % 100) + 99
    return valor

cant_prdt = int(input("ingrese la cantidad de productos a actualizar: "))

for i in range(cant_prdt):
    print("producto ", i+1)
    prdt_price = int(input("ingrese el precio del producto a actualizar: "))
    porcentaje = int(input("ingrese el porcentaje de aumento: "))
    new_price = porcentajeX(porcentaje, prdt_price)
    print("el nuevo precio es: ", new_price)
