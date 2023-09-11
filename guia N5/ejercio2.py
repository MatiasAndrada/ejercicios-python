""" 
Las   raíces   de   una   ecuación   de   segundo   grado   ax  2  +bx+c=0   son   reales   si   y   sólo   si   el 
 discriminante  dado  por  (b  2  -4ac)  no  es  negativo.  Se  desea  leer  el  valor  de  los  coeficientes  "a", 
 "b", "c" e imprimir el resultado del discriminante."""
 
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c
#Explicación discriminante
"""
El discriminante es una expresión que se encuentra dentro de la fórmula general de la ecuación de segundo grado.
El discriminante es el resultado de la operación b2 - 4ac.
Si el discriminante es mayor que cero, la ecuación tiene dos soluciones reales.
Si el discriminante es igual a cero, la ecuación tiene una solución real.
Si el discriminante es menor que cero, la ecuación no tiene soluciones reales.
 (b^2-4ac)
"""

if discriminante < 0:
    print("Las raíces de la ecuación son complejas")
else:
    print("Las raíces de la ecuación son reales")
