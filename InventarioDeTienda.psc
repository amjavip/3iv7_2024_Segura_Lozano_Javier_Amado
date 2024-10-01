Algoritmo MiniSuper
	
    Definir nombreProducto Como Caracter
    Definir idProducto, stock Como Entero
    Definir costoProducto Como Real
    Definir opcion, unidadesVendidas, stockRestante, totalVentas Como Entero
	
    // Menú de selección
    Mientras opcion <> 5 Hacer
        Escribir "1 - Registrar un nuevo producto"
        Escribir "2 - Actualizar producto existente"
        Escribir "3 - Ver el inventario"
        Escribir "4 - Generar reporte de ventas"
        Escribir "5 - Salir"
        Leer opcion
		
        Segun opcion Hacer
				// Opción 1: Ingresar nuevo producto
            Caso 1:
                Escribir "Introduce el nombre del producto:"
                Leer nombreProducto
                Escribir "Introduce el ID del producto:"
                Leer idProducto
                Escribir "Introduce la cantidad en stock:"
                Leer stock
                Escribir "Introduce el precio del producto:"
                Leer costoProducto
				
				// Opción 2: Actualizar producto
            Caso 2:
                Escribir "Introduce el ID del producto que quieres actualizar:"
                Leer idProducto
                Escribir "Introduce la nueva cantidad en stock:"
                Leer stock
				
				// Opción 3: Consultar inventario
            Caso 3:
                Escribir "Información del producto en inventario:"
                Escribir "Nombre: ", nombreProducto
                Escribir "ID: ", idProducto
                Escribir "Precio: ", costoProducto
                Escribir "Cantidad disponible: ", stock
				
				// Opción 4: Generar reporte de ventas
            Caso 4:
                Escribir "¿Cuántas unidades del producto se han vendido?"
                Leer unidadesVendidas
                stockRestante = stock - unidadesVendidas
                Escribir "El stock restante es: ", stockRestante
                totalVentas = unidadesVendidas * costoProducto
                Escribir "El total generado por las ventas es: ", totalVentas
				
				// Opción 5: Salir
            Caso 5:
                Escribir "Gracias por usar el sistema, ¡hasta pronto!"
				
        FinSegun
    FinMientras
	
FinAlgoritmo
