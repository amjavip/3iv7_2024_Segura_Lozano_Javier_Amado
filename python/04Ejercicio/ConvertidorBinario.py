import math

# Función para convertir números decimales a binarios
def ConvertirBinario(NumeroDecimal):
    i = 0
    nb = 0
    Residuo = 0
    while NumeroDecimal > 0:
        Residuo = NumeroDecimal % 2
        nb += Residuo * (10 ** i)
        NumeroDecimal = math.trunc(NumeroDecimal / 2)
        i += 1  
    
    return nb

# Función para convertir números binarios a decimales
def ConvertirDecimal(NumeroBinario):
    decimal = 0
    longitud = len(NumeroBinario)
    
    # Recorrer cada dígito del número binario
    for i in range(longitud):
        # Convertir el dígito en entero y multiplicar por 2^(posición)
        decimal += int(NumeroBinario[i]) * (2 ** (longitud - i - 1))
    
    return decimal

# Menú de opciones
def menu():
    print("Elige una opción: ")
    print("A: Convertir de decimal a binario")
    print("B: Convertir de binario a decimal")

# Programa principal
menu()
opcion = input("Introduce la opción (A-Convertir a binario, B-Convertir a decimal): ").upper()  # todo lo que se introduzca va a mayúscula

if opcion == "A":
    NumeroDecimal = int(input("Introduce el valor decimal que desees convertir a binario: "))  # Convertir a entero
    nb = ConvertirBinario(NumeroDecimal)
    
    print("El número en binario sería:", nb)
   
elif opcion == "B":
    NumeroBinario = input("Introduce el número binario que desees convertir a decimal: ")  # Mantener como cadena
    decimal = ConvertirDecimal(NumeroBinario) 
    
    print("El número en decimal ingresado sería:", decimal)
else:
    print("Error: Opción no válida")