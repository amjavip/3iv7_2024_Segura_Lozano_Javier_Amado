//DESARROLLE UN ALGORITMO QUE PERMITA REALIZAR LA ESCRITURA DE LOS PRIMEROS 100 NUMEROS NATURALES UTILIZANDO LA SENTENCIA MIENTRAS. 
Algoritmo CienMientras
	Definir N Como Entero
	Escribir "DESARROLLE UN ALGORITMO QUE PERMITA REALIZAR LA ESCRITURA DE LOS PRIMEROS 100 NUMEROS NATURALES UTILIZANDO LA SENTENCIA MIENTRAS."
	Mientras opción <> 2  Hacer
		Escribir  "1 - iniciar/repetir proceso"
		Escribir  "2 - Finalizar proceso"
		Leer opción
		Segun opción Hacer
			
		Caso 1:
	     Escribir "Ingrese el valor hasta donde quiere conocer los numero naturales"
		 Leer x
		 Si x <= 0 Entonces
			 Escribir "Error: Ingresa un valor positivo mayor a 0"
		 SiNo
			 a <- x
		 n <- 0
	    Mientras x > 0 Hacer
		x = x - 1
		n <- n + 1
		Escribir n
		Fin Mientras
		Escribir "La cantidad de numero natures entre ", a, " es de ", n
		FinSi
		Caso 2:
			Escribir "El programa finalizo con éxito"
		De Otro Modo:
			Escribir "Error: Ingresa un valor válido"
      FinSegun

    FinMientras

FinAlgoritmo
