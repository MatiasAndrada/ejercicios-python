Algoritmo suma_filas_y_columna_de_matriz
	DEFINIR Matriz, MFilas, NColumnas, VFilas, VColumnas, i,j Como Entero
	Escribir "Sistema creacion de matrices y suma de filas y columnas"
	Escribir Sin Saltar "Ingrese la cantidad de filas de la matriz:"
	Leer MFilas
	Escribir Sin Saltar "Ingrese la cantidad de columnas de la matriz:"
	Leer NColumnas
	
	Dimension Matriz[MFilas, NColumnas];	
	
	Dimension VFilas[MFilas]
	Dimension VColumnas[NColumnas]
	
	//ingreso de valores
	Para i<-0 Hasta MFilas-1 Con Paso 1 hacer // recorrer filas
		Para j<-0 Hasta NColumnas-1 Con Paso 1 Hacer// recorrer columnas
			Escribir "Ingrese los valores a sumar"
			Leer Matriz[i,j]
		FinPara
	FinPara
	
	//suma vector filas 
	Para i<-0 Hasta MFilas-1 Con Paso 1 hacer // recorrer filas
		Para j<-0 Hasta NColumnas-1 Con Paso 1 Hacer// recorrer columnas
			VFilas[i] <- VFilas[i] + Matriz[i,j]
		FinPara
	FinPara
	
	//sumavector columnas
	Para j<-0 Hasta NColumnas-1 Con Paso 1 hacer // recorrer filas
		Para i<-0 Hasta MFilas-1 Con Paso 1 Hacer// recorrer columnas
			VColumnas[j] <- VColumnas[j] + Matriz[i,j]
		FinPara
		
	FinPara
	
	//mostrar vectores
	
	// vector filas 
	Para i<-0 Hasta MFilas-1 Con Paso 1 Hacer
		Escribir "La suma de la fila"
		Escribir VFilas[i]
	FinPara
	
	
	
	
	
	//leer matriz
	Escribir "Esta es la matriz"
	Para i<-0 Hasta MFilas-1 Con Paso 1 hacer // recorrer filas
		Para j<-0 Hasta NColumnas-1 Con Paso 1 Hacer// recorrer columnas
			Escribir Sin Saltar Matriz[i,j]
		FinPara
		Escribir " "; // para asi hacer salto de linea al terminar la fila
	FinPara
	
	
FinAlgoritmo
