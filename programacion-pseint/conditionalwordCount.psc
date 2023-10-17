Algoritmo wordCount
	DEFINIR PALABRA1, PALABRA2 Como Caracter
	Escribir "Ingrese su primera palabra"
	Leer PALABRA1
	Escribir  "Ingrese la segunda palabra"
	Leer PALABRA2 
	
	lettersCountWord1 = Longitud(PALABRA1)
	lettersCountWord2 = Longitud(PALABRA)
	
	Si lettersCountWord1 > lettersCountWord2Entonces
		Escribir "Su primera palabra tiene mas caracteres que la segunda con", lettersCountWord1, "letras"
		Si lettersCountWord2 > lettersCountWord1
			Escribir "Su segunda palabra tiene mas caracteres que la segunda con", lettersCountWord2, "letras"
		Sino
			Escribir "La longitud de sus pabras es la misma con:", lettersCountWord1, "letras"
		Fin Si
	FinSi
	
	
FinAlgoritmo
