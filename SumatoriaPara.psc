Algoritmo	SumatoriaPara
	Definir total, suma, i Como Entero
	
	Escribir "Algoritmo para sumar numeros de 1 hasta n"
	Mientras opción <> 2  Hacer
		Escribir  "1 - iniciar/repetir proceso"
		Escribir  "2 - Terminar"
		Leer opción
		
		Segun opción Hacer
			
			Caso 1:
				Escribir "Ingresa el numero hasta el cual quieres que se sumen (se cuenta desde -x a -1 o de 1 a x, es decir se suma +- 1 y +- x al resultado)"
				Leer total
				x <- total
				suma <- 0
				Si total <= 0 Entonces
					Para i <- total Hasta -1 Con Paso 1 Hacer
						Escribir suma, "+", i
						suma <- suma + i 
					Fin Para
					Escribir "La suma de todos los numeros negativos entre ",x ," y -1"," es de : ", suma
					SiNo
				Para i <- 1 Hasta total Con Paso 1 Hacer
					Escribir suma, "+", i
					suma <- suma + i 
				Fin Para
				Escribir "La suma de todos los numeros consecutivos del 1 hasta ", x," es de : ", suma
			        FinSi
			caso 2:
				Escribir "El programa finalizo con exito"
			De Otro Modo:
				Escribir "Error: El valor ingresado no es válido"
		FinSegun
		
    FinMientras
	
FinAlgoritmo