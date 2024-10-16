//DESARROLLE UN ALGORITMO QUE PERMITA REALIZAR LA ESCRITURA DE LOS PRIMEROS 100 NUMEROS NATURALES UTILIZANDO LA SENTENCIA MPARA. 
Algoritmo CIENPARA
	Definir n Como Entero
	Escribir "DESARROLLE UN ALGORITMO QUE PERMITA REALIZAR LA ESCRITURA DE LOS PRIMEROS 100 NUMEROS NATURALES UTILIZANDO LA SENTENCIA PARA."
	Mientras opción <> 2  Hacer
		Escribir  "1 - iniciar/repetir proceso"
		Escribir  "2 - Terminar"
		Leer opción
		
		Segun opción Hacer
			
			Caso 1:
				Escribir "Ingrese la cantidad de numeros naturales que quieres que aparezcan"
				Leer n
				z <- n
				x <- 0 
				a <- 0 
				Si n <= 0 Entonces
					Escribir "Error: El valor a ingresar debe de ser mayor a 0"
				SiNo
				Para i<-1 Hasta n Con Paso 1 Hacer
					a <- a + 1
					x <- x + 1
					Escribir a, " : ", x
				Fin Para
				Escribir "La cantidad de numero natures del 0 al ", z, " es de ", x 
			FinSi
		Caso 2:
			Escribir "El Algortimo finalizo con exito"
		De Otro Modo:
			Escribir "Error: El valor ingresado no esta dentro del rango de valores aceptados, ingresar un valor válido para continuar"
		FinSegun
		
    FinMientras
	
FinAlgoritmo