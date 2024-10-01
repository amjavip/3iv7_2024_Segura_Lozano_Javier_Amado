Algoritmo GestionHotel

	
    // Bienvenida al sistema del hotel
    Escribir "�Bienvenido al Hotel Sol Naciente!"
    Escribir "Por favor, ingresa la capacidad total de habitaciones del hotel:"
    Leer capacidadTotal
	Si capacidaTotal <= 0 Entonces
		Escribir "Error: Ingresar un valor mayor a 0"
	FinSi
    Definir opcion, habReservada, diaEntrada, mesEntrada, a�oEntrada, diasEstancia, codigoReservacion Como Entero
    Definir habDisponibles, habOcupadas, porcentajeOcupacion Como Real
	
    Mientras opcion <> 5 Hacer
        Escribir "1 - Hacer una nueva reservaci�n"
        Escribir "2 - Cancelar una reservaci�n existente"
        Escribir "3 - Consultar disponibilidad en fechas"
        Escribir "4 - Ver reporte de ocupaci�n"
        Escribir "5 - Salir del sistema"
		
        Leer opcion
		
        Segun opcion Hacer
				// Opci�n 1: Reservar habitaci�n
            Caso 1:
                Escribir "Introduce el n�mero de la habitaci�n que deseas reservar:"
                Leer habReservada
                Si habReservada > capacidadTotal Entonces
                    Escribir "Lo sentimos, no tenemos tantas habitaciones disponibles."
                SiNo
                    Escribir "Introduce el d�a de check-in (formato DD):"
                    Leer diaEntrada
                    Escribir "Introduce el mes de check-in (formato MM):"
                    Leer mesEntrada
                    Escribir "Introduce el a�o de check-in (formato AAAA):"
                    Leer a�oEntrada
                    Escribir "�Cu�ntos d�as te hospedar�s con nosotros?"
                    Leer diasEstancia
                    Escribir "Tu c�digo de reservaci�n es: "
                    Leer codigoReservacion
                FinSi
				
				// Opci�n 2: Cancelar reservaci�n
            Caso 2:
                Escribir "Por favor, introduce tu c�digo de reservaci�n para proceder con la cancelaci�n:"
                Leer codigoReservacion
                Escribir "Tu reservaci�n ha sido cancelada. �Esperamos verte pronto de nuevo!"
				
				// Opci�n 3: Consultar fechas disponibles
            Caso 3:
                Escribir "�Qu� fecha deseas consultar? Ingresa la informaci�n a continuaci�n."
                Escribir "D�a (formato DD):"
                Leer diaConsulta
                Escribir "Mes (formato MM):"
                Leer mesConsulta
                Escribir "A�o (formato AAAA):"
                Leer a�oConsulta
                Escribir "Introduce el n�mero de habitaci�n a consultar:"
                Leer habConsultada
                Si diaConsulta = diaEntrada Y mesConsulta = mesEntrada Y a�oConsulta = a�oEntrada Y habConsultada = habReservada Entonces
                    Escribir "Lo sentimos, esa habitaci�n ya est� reservada en esa fecha."
                SiNo
                    Escribir "La habitaci�n est� disponible. �Puedes reservarla!"
                FinSi
				
				// Opci�n 4: Ver reporte de ocupaci�n
            Caso 4:
                Escribir "�Cu�ntas habitaciones est�n ocupadas actualmente?"
                Leer habOcupadas
                habDisponibles = capacidadTotal - habOcupadas
                porcentajeOcupacion = (habOcupadas * 100) / capacidadTotal
                Escribir "Actualmente el hotel tiene un ", porcentajeOcupacion, "% de ocupaci�n."
                Escribir "Quedan ", habDisponibles, " habitaciones disponibles."
				
				// Opci�n 5: Salir del sistema
            Caso 5:
                Escribir "Gracias por utilizar nuestro sistema de gesti�n. �Hasta luego!"

        FinSegun
    FinMientras

FinAlgoritmo
