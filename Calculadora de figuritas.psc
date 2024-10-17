Funcion PerimetroAreanlados (numlad, medidalad, apotema )
	Perimetro = numlad * medidalad
	Area = (apotema * perimetro) / 2
	Escribir "El valor de area y perimetro de tu poligono de ", numlad, " lados es de ", area, "u^2 y de perimetro ", Perimetro
Fin Funcion

Algoritmo CalculadoraFigurasConfunciones
	Definir  lados Como Entero
	Definir n Como Real
	Definir opcion Como Caracter
	Escribir "A - Calculadora de poligonos regulares de n lados"
	Escribir "B - Salir del programa"
	Mientras opcion <> "B" Hacer
		n <- 0
		lado <- 0
		apotema <- 0
		
		Leer opcion
		Segun opcion Hacer
			"A":
				Escribir "ingresa la cantidad de lados que tiene tu poligono regular"
				Leer n
				Si n > 4 y n < 12 Entonces
					Escribir "Ingresa cuanto mide cualquiera los lados del poligono"
					Leer lado
					Escribir "Ingresa el apotema de tu poligono regular"
					Leer apotema
					PerimetroAreanlados(n, lado, apotema)
				SiNo
					Escribir "El sistema ha sido diseñado para aceptar valores de 4 a 12 lados"
				
			FinSi
			"B":
				Escribir "El programa ha finalizado con èxito"
			De Otro Modo:
				Escribir "Error: Ingresa un valor dentro del rango permitido"
		Fin Segun
	FinMientras
	
FinAlgoritmo
