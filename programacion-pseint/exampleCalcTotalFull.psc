Algoritmo exampleCalcTotalFull
	Definir cantMoney1, cantMoney2, cantMoney3, cantMoney4, cantMoney5 Como Entero
	Definir moneda1, moneda2, moneda3, moneda4, moneda5	Como Real
	moneda1 = 1
 	moneda2 = 0.5
	moneda3 = 0.25
	moneda4 = 0.10
	moneda5 = 0.05
	
	Escribir "Calculadora de dinero con monedas"
	Escribir "Cuantas monedas de $1 tienes"
	Leer cantMoney1
	Escribir "Cuantas monedas de $0.5 tienes"
	Leer cantMoney2
	Escribir "Cuantas monedas de $0.25 tienes"
	Leer cantMoney3
	Escribir "Cuantas monedas de $0.10 tienes"
	Leer cantMoney4
	Escribir "Cuantas monedas de $0.05 tienes"
	Leer cantMoney5
	
	totalDinero <- moneda1 * cantMoney1 + moneda2 * cantMoney2 + moneda3 * cantMoney3 + moneda4 * cantMoney4 + moneda5 * cantMoney5
	
	Escribir "El dinero total que tienes es: $", totalDinero

	
	
FinAlgoritmo
