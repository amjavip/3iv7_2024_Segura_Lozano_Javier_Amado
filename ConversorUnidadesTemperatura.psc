Algoritmo  ConversionTemperatura
    Definir tempF, tempC, tempK, tempR Como Real
	Escribir "1.- Conversor de temperatura"
	Escribir "2.- Finalizar programa"
	
	Mientras OP <> 2 Hacer
		Leer OP
		tempC <- 0
		tempf <- 0
		tempK <- 0
		TempR <- 0
		Segun OP Hacer
	Caso 1:
    Escribir "Ingrese la temperatura en grados Fahrenheit: "
    Leer tempF
    Escribir "Seleccione la conversión que desea realizar:"
    Escribir "1. Fahrenheit a Celsius"
    Escribir "2. Fahrenheit a Kelvin"
    Escribir "3. Fahrenheit a Rankine"
    Leer opcion
    
    Segun opcion Hacer
        Caso 1:
            // Fahrenheit a Celsius
            tempC = (tempF - 32) * 5 / 9
            Escribir "La temperatura en grados Celsius es: ", tempC
        Caso 2:
            // Fahrenheit a Kelvin
            tempK = (tempF - 32) * 5 / 9 + 273.15
            Escribir "La temperatura en grados Kelvin es: ", tempK
        Caso 3:
            // Fahrenheit a Rankine
            tempR = tempF + 459.67
            Escribir "La temperatura en grados Rankine es: ", tempR
        De Otro Modo:
            Escribir "Erro: El valor ingresado no está dentro del rango de valores permitidos por el sistema"
    FinSegun
Caso 2: Escribir "El programa finalizó con exito"
De Otro Modo:
	Escribir "Error: El valor ingresado no está dentro del rango de valores permitidos por el sistema"
FinSegun
FinMientras
FinAlgoritmo
