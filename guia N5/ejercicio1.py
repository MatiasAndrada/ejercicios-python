"""Escribir un programa que permita calcular el precio de un artículo para un año dado,
considerando que la inflación es del 4 por 100 anual."""

tasa_anual = 4

precio_actual = float(input("Ingrese el precio actual del producto: "))
año_actual = int(input("Ingrese el año actual: "))
año_futuro = int(input("Ingrese el año futuro: "))
años = año_futuro - año_actual


formula_precio = precio_actual * (1 + (tasa_anual/100)) ** años

print(f"El precio del producto en el año {año_futuro} será de ${formula_precio:.2f}")

