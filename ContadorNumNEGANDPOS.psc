Algoritmo  ContarPositivosNegativos
    cantidadPositivos = 0
    cantidadNegativos = 0
	cantidadCeros = 0
    Escribir "Ingrese la cantidad de números que va a introducir: "
    Leer cantidadNumeros
    
    Para i=1 Hasta cantidadNumeros Con Paso 1 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer num
        
        Si num > 0 Entonces
            cantidadPositivos = cantidadPositivos + 1
        SiNo
            Si num < 0 Entonces
                cantidadNegativos = cantidadNegativos + 1
			SiNo
				Si num = 0 Entonces 
					Escribir "El cero no esta dentro de los numero positivos ni negativos por lo que se agregara un nuevo contador que se escribira al final de las respuestas"
					cantidadCeros = cantidadCeros + 1
				FinSi
            FinSi
        FinSi
    FinPara
    
    Escribir "Cantidad de números positivos: ", cantidadPositivos
    Escribir "Cantidad de números negativos: ", cantidadNegativos
	Si cantidadCeros > 0 Entonces
		Escribir "Cantidad de ceros en la cadena de numeros ingresados es de : ", cantidadCeros
	FinSi
FinAlgoritmo
