# Inicializamos la lista de alumnos
import tkinter as Tk
from tkinter import simpledialog, messagebox
alumnos = []

# Función para registrar un alumno
def registraralumno():
    boleta = input("Ingresa la boleta del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    apelpat = input("Ingresa el apellido paterno del alumno: ")
    apelmat = input("Ingresa el apellido materno del alumno: ")
    fechn = input("Ingresa la fecha de nacimiento (día, mes, año): ")

    # Solicitar tres calificaciones
    calificaciones = []
    for i in range(1, 4): 
        while True:  # Para asegurarse de que se ingresa un número válido
            try:
                parcial = float(input(f"Ingrese la calificación del parcial {i}: "))
                calificaciones.append(parcial)
                break  # Salimos del bucle si la entrada es válida
            except ValueError:
                print("Por favor, ingresa un número válido para la calificación.")

    # Definimos al alumno como un diccionario
    alumno = {
        "Boleta": boleta, 
        "Nombre": nombre,
        "Apellido paterno": apelpat,
        "Apellido materno": apelmat,
        "Fecha de nacimiento": fechn,
        "Calificaciones": calificaciones
    }

    # Agregamos el alumno a la lista de alumnos
    alumnos.append(alumno)
    print("¡El alumno se registró correctamente!")

# Función para consultar todos los alumnos
def consulta():
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(f"Boleta: {alumno['Boleta']}, Nombre: {alumno['Nombre']} {alumno['Apellido paterno']} {alumno['Apellido materno']}, Fecha de nacimiento: {alumno['Fecha de nacimiento']}, Calificaciones: {alumno['Calificaciones']}")

# Función para editar los datos de un alumno
def editar_alumno():
    boleta = input("Ingrese la boleta que desea editar: ")
    for alumno in alumnos:
        if alumno['Boleta'] == boleta:
            alumno['Nombre'] = input(f"Ingresa un nuevo nombre (actual: {alumno['Nombre']}) o presiona enter para mantenerlo: ") or alumno['Nombre']
            alumno['Apellido paterno'] = input(f"Ingresa un nuevo apellido paterno (actual: {alumno['Apellido paterno']}) o presiona enter para mantenerlo: ") or alumno['Apellido paterno']
            alumno['Apellido materno'] = input(f"Ingresa un nuevo apellido materno (actual: {alumno['Apellido materno']}) o presiona enter para mantenerlo: ") or alumno['Apellido materno']
            alumno['Fecha de nacimiento'] = input(f"Ingresa una nueva fecha de nacimiento (actual: {alumno['Fecha de nacimiento']}) o presiona enter para mantenerla: ") or alumno['Fecha de nacimiento']
            
            # Editamos las calificaciones
            for i in range(3):
                nueva_calificacion = input(f"Ingrese una nueva calificación para el parcial {i+1} (actual: {alumno['Calificaciones'][i]}) o presiona enter para mantenerla: ")
                if nueva_calificacion:
                    alumno['Calificaciones'][i] = float(nueva_calificacion)
            print("¡Datos del alumno actualizados!")
            return
    print("Alumno no encontrado.")

# Función para eliminar un alumno
def eliminar_alumno():
    boleta = input("Ingrese la boleta del alumno que desea eliminar: ")
    for alumno in alumnos:
        if alumno['Boleta'] == boleta:
            alumnos.remove(alumno)
            print("Alumno eliminado exitosamente.")
            return
    print("Alumno no encontrado.")

# Función principal del menú
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar alumno")
        print("2. Consultar lista de alumnos")
        print("3. Editar alumno")
        print("4. Eliminar alumno")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registraralumno()
        elif opcion == "2":
            consulta()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 5.")

# Ejecutamos el programa
main()