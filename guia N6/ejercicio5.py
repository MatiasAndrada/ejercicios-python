# En un almacén se  descuenta  20% del  precio  al cliente  si el valor a pagarse es mayor a $  200  . Dado un valor de precio, muestre lo que debe  pagar  el cliente. 

min_price_for_discount = 200
discount = 20

price = float(input("Ingrese el precio: "))
if price > min_price_for_discount:
    print(f"El precio final con descuento aplicado es:  {price*(1-discount/100):.2f}")
else:
    print(f"El precio final sin descuento es: {price:.2f}")
    