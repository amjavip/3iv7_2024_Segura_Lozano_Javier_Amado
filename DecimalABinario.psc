Algoritmo DecimalABinario
	Escribir "Ingrese numero el cual se quiere convertir en binario "
	Leer x
	nb = 0
	i = 1
	
	Mientras (x > 0) Hacer
		residuo = x % 2
		nb = nb + residuo * i
		x = trunc(x/2)
		i =  i * 10
	FinMientras
	
	Escribir "Numero Binario: ",nb
FinAlgoritmo