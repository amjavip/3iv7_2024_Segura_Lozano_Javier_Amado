#suma de matrices 3 x 3
def ingresa_matriz():
    matriz = []
    print("introduce los valores de la matriz 3x3")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input("elemento [(i+1)][(j+1)]"))
            fila.apend(valor)
        matriz.append(fila)
    return matriz


def sumar_matriz(matriz1, matriz2):
    matriz_suma = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.apend(matriz1[i][j]+matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

def imprimir_suma(matriz):
    for fila in matriz:
        print(fila)
#programa principal
print ("matriz 1: ")
matriz1 = ingresa_matriz()
print ("matriz 2: ")
matriz2 = ingresa_matriz()
matriz_resultado = sumar_matriz(matriz1, matriz2)
print = ("el resultado es : ")
imprimir_suma(matriz_resultado)