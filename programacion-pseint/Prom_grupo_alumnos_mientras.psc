Algoritmo Prom_grupo_alumnos
	Definir alumnos, edad, e_total Como Entero
	Definir e_prom Como Real	
	Escribir "Ingrese el numero de alumnos:"
	Leer alumnos
	count = 1
	Mientras alumnos >= count Hacer
		Escribir "Por favor ingrese la edad del alumno " count " de " alumnos
		Leer edad
		e_total <- e_total + edad
		count <- count + 1
	Fin Mientras
	e_prom <- e_total / alumnos
	Escribir "La edad prom es:" e_prom 
	
	
FinAlgoritmo
