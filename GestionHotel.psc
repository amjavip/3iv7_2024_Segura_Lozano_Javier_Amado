Algoritmo GestionHotel

	
    // Bienvenida al sistema del hotel
    Escribir "¡Bienvenido al Hotel Sol Naciente!"
    Escribir "Por favor, ingresa la capacidad total de habitaciones del hotel:"
    Leer capacidadTotal
	Si capacidaTotal <= 0 Entonces
		Escribir "Error: Ingresar un valor mayor a 0"
	FinSi
    Definir opcion, habReservada, diaEntrada, mesEntrada, añoEntrada, diasEstancia, codigoReservacion Como Entero
    Definir habDisponibles, habOcupadas, porcentajeOcupacion Como Real
	
    Mientras opcion <> 5 Hacer
        Escribir "1 - Hacer una nueva reservación"
        Escribir "2 - Cancelar una reservación existente"
        Escribir "3 - Consultar disponibilidad en fechas"
        Escribir "4 - Ver reporte de ocupación"
        Escribir "5 - Salir del sistema"
		
        Leer opcion
		
        Segun opcion Hacer
				// Opción 1: Reservar habitación
            Caso 1:
                Escribir "Introduce el número de la habitación que deseas reservar:"
                Leer habReservada
                Si habReservada > capacidadTotal Entonces
                    Escribir "Lo sentimos, no tenemos tantas habitaciones disponibles."
                SiNo
                    Escribir "Introduce el día de check-in (formato DD):"
                    Leer diaEntrada
                    Escribir "Introduce el mes de check-in (formato MM):"
                    Leer mesEntrada
                    Escribir "Introduce el año de check-in (formato AAAA):"
                    Leer añoEntrada
                    Escribir "¿Cuántos días te hospedarás con nosotros?"
                    Leer diasEstancia
                    Escribir "Tu código de reservación es: "
                    Leer codigoReservacion
                FinSi
				
				// Opción 2: Cancelar reservación
            Caso 2:
                Escribir "Por favor, introduce tu código de reservación para proceder con la cancelación:"
                Leer codigoReservacion
                Escribir "Tu reservación ha sido cancelada. ¡Esperamos verte pronto de nuevo!"
				
				// Opción 3: Consultar fechas disponibles
            Caso 3:
                Escribir "¿Qué fecha deseas consultar? Ingresa la información a continuación."
                Escribir "Día (formato DD):"
                Leer diaConsulta
                Escribir "Mes (formato MM):"
                Leer mesConsulta
                Escribir "Año (formato AAAA):"
                Leer añoConsulta
                Escribir "Introduce el número de habitación a consultar:"
                Leer habConsultada
                Si diaConsulta = diaEntrada Y mesConsulta = mesEntrada Y añoConsulta = añoEntrada Y habConsultada = habReservada Entonces
                    Escribir "Lo sentimos, esa habitación ya está reservada en esa fecha."
                SiNo
                    Escribir "La habitación está disponible. ¡Puedes reservarla!"
                FinSi
				
				// Opción 4: Ver reporte de ocupación
            Caso 4:
                Escribir "¿Cuántas habitaciones están ocupadas actualmente?"
                Leer habOcupadas
                habDisponibles = capacidadTotal - habOcupadas
                porcentajeOcupacion = (habOcupadas * 100) / capacidadTotal
                Escribir "Actualmente el hotel tiene un ", porcentajeOcupacion, "% de ocupación."
                Escribir "Quedan ", habDisponibles, " habitaciones disponibles."
				
				// Opción 5: Salir del sistema
            Caso 5:
                Escribir "Gracias por utilizar nuestro sistema de gestión. ¡Hasta luego!"

        FinSegun
    FinMientras

FinAlgoritmo
