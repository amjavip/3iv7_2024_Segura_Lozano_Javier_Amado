Algoritmo EcuacionesCuadraticas
	Definir a, b, c Como Real
	discriminante <- 0
	Escribir "Ingresar los valores de a, b, c de la ecuacion (ax^2 + bx + c)"
	Escribir "Ingresa a"
	Leer a
	Escribir "Ingresa b"
	Leer b
	Escribir "Ingresa b"
	Leer c
	discriminante <- b^2 - 4*a*c
	Si discriminante < 0 Entonces
		Escribir "No tiene soluciones reales, solo imaginarias"
	SiNo
		x1 = (-b + raiz(discriminante)) / (2*a)
		x2 = (-b - raiz(discriminante)) / (2*a)
		Escribir "Las soluciones a esta ecuacion serian ", x1, " y ", x2
	FinSi
FinAlgoritmo
