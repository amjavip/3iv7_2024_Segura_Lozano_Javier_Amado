# Ejercicio para entender este tipo de listas

# Una lista es muy parecida a un arreglo, solo que una estructutura mas versail la cual puede manejar (enteros, flotantes, cadenas, caracteres, etc)

# Vmos a crear una lista de estudiantes

estudiantes = ["Ana", "Paco", "Hugo", "Luis"]

# Metodos propios: 
# apend(x), agrega un valor al final
# inser(i, x), inserta un elemento en una posicion especifica
# remove(x), elimin aun elemento x del primer elemento de una lista

#agregar uno
estudiantes.append("diana")
print("lista de estudiantes", estudiantes)

# Eliminar uno
estudiantes.remove("Hugo")
print("lista de estudiantes", estudiantes)