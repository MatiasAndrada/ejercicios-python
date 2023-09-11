#Hacer programa que pida al usuario la altura en cm y el peso en kg y calcule el IMC

#Entrada de datos
altura = float(input("Ingrese su altura en cm: "))
peso = float(input("Ingrese su peso en kg: "))
#Proceso
imc = peso / (altura/100)**2  
#Salida
print("Su IMC es: ", imc)

#Dar tabla de como esta la persona

if imc < 18.5:
    print("Usted esta bajo de peso")
elif imc >= 18.5 and imc < 25:
    print("Usted esta en su peso normal")
elif imc >= 25 and imc < 30:
    print("Usted esta en sobrepeso")
elif imc >= 30 and imc < 35:
    print("Usted tiene obesidad grado 1")
elif imc >= 35 and imc < 40:
    print("Usted tiene obesidad grado 2")
else:
    print("Usted tiene obesidad grado 3")
    
    