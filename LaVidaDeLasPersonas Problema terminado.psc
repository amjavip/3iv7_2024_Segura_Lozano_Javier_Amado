Algoritmo LaVidaDeLasPersonas
	//Variables
	Definir NumeroPersonas, A�osAConsultar, TPersonasVivas, EdadJoven, EdadVieja, Edad, i, x, l, z Como Entero
	//Limpiar las Variables
	NumeroPersonas <- 0
	TPersonasVivas <- 0
	//Meter la lista de personas dadas por el profe
	Escribir "Ingresa el numero del personas de la lista"
	Leer NumeroPersonas
	//Crear arreglitos
	Dimension A�oNacimiento[NumeroPersonas]
	Dimension A�oFallecimiento[NumeroPersonas]
	//Estructura para meter los datos
	Para i <- 1 Hasta NumeroPersonas Con Paso 1 Hacer
		Escribir "Ingresa el a�o de nacimiento de la persona numero", i
		Leer A�oNacimiento[i]
		Escribir "Ingresa el a�o de fallecimiento de la persona numero ", i
		Leer A�oFallecimiento[i]
		Si A�oFallecimiento[i] - A�oNacimiento[i] < 0 Entonces
			Escribir "La persona no puede morir antes de nacer"
		FinSi
	Fin Para
	//A�os a consultar para la lista dada
	Escribir "Ingresa el numero de a�os a consultar"
	Leer A�osAConsultar
	Dimension A�oIngresado[A�osAConsultar]
	Si A�osAConsultar <= 0 Entonces
		Escribir "Ingresar un valor v�lido"
	SiNo
		Para X <- 1 Hasta A�osAConsultar Con Paso 1 Hacer
			Escribir "�De que a�o desea conocer los datos?"
			Leer A�oIngresado[X]
		FinPara
		Para l <- 1 Hasta A�osAConsultar Con Paso 1 Hacer
				TPersonasVivas <- 0
				EdadJoven <- 9999
				EdadVieja <- 0
				Para Z <- 1 Hasta NumeroPersonas Con Paso 1 Hacer
					//Saber cuantas personas vivas hab�a
					Si A�oNacimiento[Z] <= A�oIngresado[l] Y A�oFallecimiento[Z] >= A�oIngresado[l] Entonces
						TPersonasVivas = TPersonasVivas + 1
					FinSi
					
					Edad = A�oIngresado[l] - A�oNacimiento[Z]
					//Calcular la persona mas joven
					Si Edad < EdadJoven y Edad >= 0 Entonces
						EdadJoven <- Edad
					FinSi
					//Calcular la persona mas vieja
					Si Edad >= EdadVieja y Edad >= EdadJoven y 0 >= A�oIngresado[l]-A�oFallecimiento[Z] Entonces
						EdadVieja <- Edad
					FinSi
				Fin Para
				Escribir "En el a�o ", A�oIngresado[l], " habia ", TPersonasVivas," personas con vida." 
				Si TPersonasVivas <= 0 Entonces
					Escribir "No habia personas vivas, por lo tanto no habia ni personas mas jovenes ni mas longevas"
				SiNo
					Escribir "La persona mas joven tenia ", EdadJoven, " a�os"
					Escribir "y"
					Escribir "La persona mas longeva tenia ", EdadVieja, " a�os"
				FinSi
				
			FinPara
			
		
	FinSi
FinAlgoritmo
