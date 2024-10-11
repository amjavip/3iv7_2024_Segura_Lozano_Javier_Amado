//MODIFICA EL ALGORITMO ANTERIOR PARA QUE SÓLO MUESTRE LOS NÚMEROS IMPARES.
Algoritmo CienImpares
	Definir N Como Entero
	Escribir "MODIFICA EL ALGORITMO ANTERIOR PARA QUE SÓLO MUESTRE LOS NÚMEROS IMPARES."
	Mientras opción <> 2  Hacer
		Escribir  "1 - iniciar/repetir proceso"
		Escribir  "2 - Terminar"
		Leer opción
		
		Segun opción Hacer
			
			Caso 1:
				Escribir "Ingrese el límite para que aparezcan números impares"
				Leer x
				Si x <= 0 Entonces
					numf <- x
					n <- -1
					numc <- 0 
					a <- 0
					Para i <- x Hasta 0 Con Paso 1 Hacer
						n <- n + 1
						Si n % 2 <> 0 Entonces
							numc = numc +1
							Escribir numc," : ", -n
							a = a + 1
						Fin Si
					Fin Para
					Escribir "La cantidad de numero pares entre 0 y ", numf, " es de ", a
				SiNo
				numf <- x
				n <- -1
				numc <- 0 
				a <- 0
				Para i <- 0 Hasta x Con Paso 1 Hacer
					n <- n + 1
					Si n % 2 <> 0 Entonces
						numc = numc +1
						Escribir numc," : ", n
						a = a + 1
					Fin Si
				Fin Para
				Escribir "La cantidad de numero pares entre 0 y ", numf, " es de ", a
			FinSi
			Caso 2: 
				Escribir "El algoritmo ha finalizado con exito"
			De Otro Modo:
				Escribir "Error: El valor introducido no esta detro del rango de valores válidos, favor de ingresar un valor válido"
		FinSegun
		
    FinMientras
	
FinAlgoritmo