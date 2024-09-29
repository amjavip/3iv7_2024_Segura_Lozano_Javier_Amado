Algoritmo LaVidaDeLasPersonas
	//Variables
	Definir NumeroPersonas, AñosAConsultar, TPersonasVivas, EdadJoven, EdadVieja, Edad, i, x, l, z Como Entero
	//Limpiar las Variables
	NumeroPersonas <- 0
	TPersonasVivas <- 0
	//Meter la lista de personas dadas por el profe
	Escribir "Ingresa el numero del personas de la lista"
	Leer NumeroPersonas
	//Crear arreglitos
	Dimension AñoNacimiento[NumeroPersonas]
	Dimension AñoFallecimiento[NumeroPersonas]
	//Estructura para meter los datos
	Para i <- 1 Hasta NumeroPersonas Con Paso 1 Hacer
		Escribir "Ingresa el año de nacimiento de la persona numero", i
		Leer AñoNacimiento[i]
		Escribir "Ingresa el año de fallecimiento de la persona numero ", i
		Leer AñoFallecimiento[i]
		Si AñoFallecimiento[i] - AñoNacimiento[i] < 0 Entonces
			Escribir "La persona no puede morir antes de nacer"
		FinSi
	Fin Para
	//Años a consultar para la lista dada
	Escribir "Ingresa el numero de años a consultar"
	Leer AñosAConsultar
	Dimension AñoIngresado[AñosAConsultar]
	Si AñosAConsultar <= 0 Entonces
		Escribir "Ingresar un valor válido"
	SiNo
		Para X <- 1 Hasta AñosAConsultar Con Paso 1 Hacer
			Escribir "¿De que año desea conocer los datos?"
			Leer AñoIngresado[X]
		FinPara
		Para l <- 1 Hasta AñosAConsultar Con Paso 1 Hacer
				TPersonasVivas <- 0
				EdadJoven <- 9999
				EdadVieja <- 0
				Para Z <- 1 Hasta NumeroPersonas Con Paso 1 Hacer
					//Saber cuantas personas vivas había
					Si AñoNacimiento[Z] <= AñoIngresado[l] Y AñoFallecimiento[Z] >= AñoIngresado[l] Entonces
						TPersonasVivas = TPersonasVivas + 1
					FinSi
					
					Edad = AñoIngresado[l] - AñoNacimiento[Z]
					//Calcular la persona mas joven
					Si Edad < EdadJoven y Edad >= 0 Entonces
						EdadJoven <- Edad
					FinSi
					//Calcular la persona mas vieja
					Si Edad >= EdadVieja y Edad >= EdadJoven y 0 >= AñoIngresado[l]-AñoFallecimiento[Z] Entonces
						EdadVieja <- Edad
					FinSi
				Fin Para
				Escribir "En el año ", AñoIngresado[l], " habia ", TPersonasVivas," personas con vida." 
				Si TPersonasVivas <= 0 Entonces
					Escribir "No habia personas vivas, por lo tanto no habia ni personas mas jovenes ni mas longevas"
				SiNo
					Escribir "La persona mas joven tenia ", EdadJoven, " años"
					Escribir "y"
					Escribir "La persona mas longeva tenia ", EdadVieja, " años"
				FinSi
				
			FinPara
			
		
	FinSi
FinAlgoritmo
