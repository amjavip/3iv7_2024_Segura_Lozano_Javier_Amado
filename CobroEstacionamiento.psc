Algoritmo  CobroEstacionamiento
	// Variables para guardar la hora de entrada y salida
	Definir horaEntrada, minutoEntrada, horaSalida, minutoSalida Como Entero
	Definir totalMinutos, costoTotal Como Real
	
	// Solicitar hora de entrada
	Escribir "Ingrese la hora de entrada (formato 24 horas):"
	Leer horaEntrada
	Si horaEntrada > 24 Entonces
		Escribir "Error: La hora de entrada no puede ser mayor a 24h"
	SiNo
		Escribir "Ingrese los minutos de entrada:"
		Leer minutoEntrada
		Si minutoEntrada > 60 Entonces
			Escribir "Error: Los minutos de entrada no puede ser mayor a 60min"
		SiNo
			// Solicitar hora de salida
			Escribir "Ingrese la hora de salida (formato 24 horas):"
			Leer horaSalida
			Si horaSalida > 24 Entonces
				Escribir "Error: La hora de salida no puede ser mayor a 24h"
				
			FinSi
			Escribir "Ingrese los minutos de salida:"
			Leer minutoSalida
			Si minutoSalida > 60 Entonces
				Escribir "Error: Los minutos de salida no puede ser mayor a 60min"
			SiNo
				// Verificar que la hora de salida no sea menor a la de entrada (solo un día)
				Si (horaSalida < horaEntrada) O ((horaSalida = horaEntrada) Y (minutoSalida < minutoEntrada)) Entonces
					Escribir "Error: La hora de salida no puede ser menor que la hora de entrada en el mismo día."
				FinSi
			FinSi
		FinSi
	FinSi
	
// Calcular el tiempo total en minutos
totalMinutos = (horaSalida * 60 + minutoSalida) - (horaEntrada * 60 + minutoEntrada)

// Calcular el costo total
Si totalMinutos < 15 Entonces
	// Si estaciona menos de 15 minutos, no se cobra nada
	costoTotal = 0
Sino
	// Calcular horas completas y fracciones de 15 minutos
	Definir horasCompletas, bloquesDeQuinceMinutos Como Entero
	horasCompletas = Trunc(totalMinutos / 60)  // Asegurar que horas completas sea entero
	
	// Calcular minutos adicionales después de horas completas
	Definir minutosRestantes Como Entero
	minutosRestantes = totalMinutos % 60
	
	// Calcular el costo por las horas completas
	costoTotal = horasCompletas * 15.0  // Multiplicamos por 15 como real para evitar errores de tipo
	
	// Calcular el costo adicional por fracciones de 15 minutos
	Si minutosRestantes > 0 Entonces
		// Dividimos los minutos restantes en bloques de 15 minutos
		bloquesDeQuinceMinutos = Trunc(minutosRestantes / 15)  // Asegurar que sea un entero
		
		// Si hay un residuo que no forma un bloque completo de 15 minutos, se cobra 6 pesos adicionales
		Si minutosRestantes % 15 > 0 Entonces
			bloquesDeQuinceMinutos = bloquesDeQuinceMinutos + 1
		FinSi
		
		// Se añade el costo por bloques de 15 minutos
		costoTotal = costoTotal + (bloquesDeQuinceMinutos * 6.0)  // Multiplicamos por 6 como real
	FinSi
FinSi

// Mostrar el costo total
Escribir "El costo total por el estacionamiento es: ", costoTotal, " pesos"
FinAlgoritmo

