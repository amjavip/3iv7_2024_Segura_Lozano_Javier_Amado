#crear funcion que se encargue de sumar dos arreglos
def sumar_arreglos(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        print("los arreglos deben de tener la misma longitud")
        return None
    else:
        suma = []
        for i in range(len(arreglo1)):
            suma.append(arreglo1[i]+arreglo2[i])
            #.append sirve para agregar agregar a la posicion siguiente ,es decir i + 1
            return suma
#programa principal
arreglo1 = []
arreglo2 = []
n = int(input("introduce el tamaño del arreglo: "))
print("introduce los elementos del primer arreglo")
for i in range(n):
    num = float(input("ingresa el elemento (i + 1): "))
    arreglo1.append(num)

print("introduce los elementos del segundo arreglo")
for i in range(n):
    num = float(input("ingresa el elemento (i + 1): "))
    arreglo2.append(num)

resultado = sumar_arreglos(arreglo1, arreglo2)
if resultado is not None:
    print ("la suma de los 2 reaultados es: ", resultado)