

Algoritmo Conversiones
	Escribir "Opciones: "
	Escribir "1.- Ingresar la cantidad en pies (ft) que desea convertir"
	Escribir "2.- Tablas de medidas"
	Escribir "3.- Finalizar el proceso "
	
	Mientras A <> 3  Hacer
		Conver <- 0
		Pies <- 0
		Leer opcion
		Segun opcion Hacer
			1:
				Escribir "Ingresa a la que medida quieres convertir"
				Escribir "1.- Pulgadas"
				Escribir "2.- Metros"
				Escribir "3.- Yardas"
				Escribir "4.- Centimetros"
				Leer op
				Segun op Hacer
					1:
						Escribir "Ingresa tu cantidad en pies"
						Leer Pies
						Conver = Pies * 12
						Escribir Pies,  "Pies son :", Conver, "pulgadas"
					2:
						Escribir "Ingresa tu cantidad en pies"
						Leer Pies
						Conver = Pies * 0.3048
						Escribir Pies,  "Pies son :", Conver, "metros"
					3:
						Escribir "Ingresa tu cantidad en pies"
						Leer Pies
						Conver = Pies / 3
						Escribir Pies,  "Pies son :", Conver, "Yardas"
					4:
						Escribir "Ingresa tu cantidad en pies"
						Leer Pies
						Conver = Pies * 30.48
						Escribir Pies,  "Pies son :", Conver, "Centimetros"
					De Otro Modo:
						Escribir "Error: Valor fuera de rango (1 - 4)"
				Fin Segun
			2:
				Escribir "1 pie = 12 pulgadas"
				Escribir "1 pie = 0.3048 metros"
				Escribir "1 Pie = 0.33333 Yardas"
				Escribir "1 Pie = 30.48 centimetros"
			3:
				Escribir "El programa ha finalizado con exito"
			De Otro Modo:
				Escribir "Error: Valor fuera de rango (1 - 3)"
		Fin Segun
	FinMientras

FinAlgoritmo
