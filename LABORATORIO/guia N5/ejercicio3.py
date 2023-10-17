"""
Calcular precio total de una computadora y una impresora:
- Suma de los costos de los materiales
- Los porcentaje de ganancia del vendedor (Suponer que es de 12% pra la computadora y 7% para la impresora)
- 21% IVA

"""

IVA = 21
costo_computadora = float(input("Ingrese el costo de la computadora: "))
costo_impresora = float(input("Ingrese el costo de la impresora: "))
#Ganancia
ganancia_computadora = costo_computadora * 0.12
print (f"La ganancia de la computadora es de ${ganancia_computadora:.2f}")
ganancia_impresora = costo_impresora * 0.07
print (f"La ganancia de la impresora es de ${ganancia_impresora:.2f}")
#Precio total con ganancia
precio_con_ganancia_computadora = costo_computadora + ganancia_computadora
precio_con_ganancia_impresora = costo_impresora + ganancia_impresora
#Precio total con ganancia e IVA
precio_con_ganancia_iva_computadora = precio_con_ganancia_computadora * (1 + (IVA/100))
precio_con_ganancia_iva_impresora = precio_con_ganancia_impresora * (1 + (IVA/100))

#Precio total
precio_total = precio_con_ganancia_iva_computadora + precio_con_ganancia_iva_impresora
print (f"El precio total es de ${precio_total:.2f}")
print (f"El precio total de la computadora es de ${precio_con_ganancia_iva_computadora:.2f}")
print (f"El precio total de la impresora es de ${precio_con_ganancia_iva_impresora:.2f}")
