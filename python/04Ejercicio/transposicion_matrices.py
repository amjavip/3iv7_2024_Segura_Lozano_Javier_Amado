#se crea la matriz dependiendo de su tamaño (5x5) o (3x3)
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
#para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
#funcion de tranpocision
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = [[0] * filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]
    
    return matriz_transpuesta
#programa principal
tamaño = int(input("Ingrese el tamaño de la matriz (3 o 5): "))
if tamaño not in [3, 5]:
    print("Por favor, ingrese un tamaño válido (3 o 5).")
else:
    matriz = crear_matriz(tamaño, tamaño)
    
    print("\nMatriz original:")
    imprimir_matriz(matriz)
    
    matriz_transpuesta = transponer_matriz(matriz)
    
    print("\nMatriz transpuesta:")
    imprimir_matriz(matriz_transpuesta)
