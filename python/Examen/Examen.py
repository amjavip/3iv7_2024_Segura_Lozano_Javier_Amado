import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os

ARCHIVO = "audifonos.txt"
audifonos = []
def cargar_datos_iniciales():
    # Registros predefinidos de audífonos
    audifonos_iniciales = [
        {"modelo": "Sony WH-1000XM4", "marca": "Sony", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "30 horas", "cancelacion_ruido": "Sí", "precio": "350", "color": "Negro"},
        {"modelo": "AirPods Pro", "marca": "Apple", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "4.5 horas", "cancelacion_ruido": "Sí", "precio": "250", "color": "Blanco"},
        {"modelo": "Bose QuietComfort 35 II", "marca": "Bose", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "20 horas", "cancelacion_ruido": "Sí", "precio": "300", "color": "Plateado"},
        {"modelo": "Jabra Elite 75t", "marca": "Jabra", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "7.5 horas", "cancelacion_ruido": "No", "precio": "180", "color": "Negro"},
        {"modelo": "Sennheiser HD 450BT", "marca": "Sennheiser", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "30 horas", "cancelacion_ruido": "Sí", "precio": "200", "color": "Blanco"},
        {"modelo": "Anker Soundcore Life Q30", "marca": "Anker", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "40 horas", "cancelacion_ruido": "Sí", "precio": "80", "color": "Negro"},
        {"modelo": "Beats Solo Pro", "marca": "Beats", "tipo": "On-ear", "inalambrico": "Sí", "bateria": "22 horas", "cancelacion_ruido": "Sí", "precio": "300", "color": "Rojo"},
        {"modelo": "Samsung Galaxy Buds Pro", "marca": "Samsung", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "5 horas", "cancelacion_ruido": "Sí", "precio": "200", "color": "Negro"},
        {"modelo": "Sony WF-1000XM3", "marca": "Sony", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "6 horas", "cancelacion_ruido": "Sí", "precio": "230", "color": "Plateado"},
        {"modelo": "Bang & Olufsen Beoplay H9", "marca": "Bang & Olufsen", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "25 horas", "cancelacion_ruido": "Sí", "precio": "500", "color": "Gris"},
        {"modelo": "Audio-Technica ATH-M50xBT", "marca": "Audio-Technica", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "40 horas", "cancelacion_ruido": "No", "precio": "180", "color": "Negro"},
        {"modelo": "Bose Sport Earbuds", "marca": "Bose", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "5 horas", "cancelacion_ruido": "No", "precio": "180", "color": "Azul"},
        {"modelo": "JBL Tune 750BTNC", "marca": "JBL", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "15 horas", "cancelacion_ruido": "Sí", "precio": "130", "color": "Negro"},
        {"modelo": "Marshall Major IV", "marca": "Marshall", "tipo": "On-ear", "inalambrico": "Sí", "bateria": "80 horas", "cancelacion_ruido": "No", "precio": "150", "color": "Negro"},
        {"modelo": "Sennheiser Momentum 3", "marca": "Sennheiser", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "17 horas", "cancelacion_ruido": "Sí", "precio": "400", "color": "Negro"},
        {"modelo": "AKG N60NC", "marca": "AKG", "tipo": "On-ear", "inalambrico": "Sí", "bateria": "15 horas", "cancelacion_ruido": "Sí", "precio": "150", "color": "Negro"},
        {"modelo": "Sony XB900N", "marca": "Sony", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "30 horas", "cancelacion_ruido": "Sí", "precio": "250", "color": "Azul"},
        {"modelo": "Pioneer DJ HDJ-X10", "marca": "Pioneer", "tipo": "Over-ear", "inalambrico": "No", "bateria": "N/A", "cancelacion_ruido": "No", "precio": "350", "color": "Negro"},
        {"modelo": "Razer Opus", "marca": "Razer", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "25 horas", "cancelacion_ruido": "Sí", "precio": "200", "color": "Azul"},
        {"modelo": "OneOdio A70", "marca": "OneOdio", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "25 horas", "cancelacion_ruido": "No", "precio": "60", "color": "Negro"},
        {"modelo": "Grado SR80e", "marca": "Grado", "tipo": "On-ear", "inalambrico": "No", "bateria": "N/A", "cancelacion_ruido": "No", "precio": "100", "color": "Negro"},
        {"modelo": "Shure AONIC 50", "marca": "Shure", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "20 horas", "cancelacion_ruido": "Sí", "precio": "400", "color": "Negro"},
        {"modelo": "JLab Audio JBuds Air", "marca": "JLab", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "6 horas", "cancelacion_ruido": "No", "precio": "50", "color": "Negro"},
        {"modelo": "Anker Soundcore Liberty Air 2", "marca": "Anker", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "7 horas", "cancelacion_ruido": "No", "precio": "100", "color": "Blanco"},
        {"modelo": "Jaybird Vista", "marca": "Jaybird", "tipo": "In-ear", "inalambrico": "Sí", "bateria": "6 horas", "cancelacion_ruido": "No", "precio": "180", "color": "Negro"},
        {"modelo": "Skullcandy Crusher ANC", "marca": "Skullcandy", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "24 horas", "cancelacion_ruido": "Sí", "precio": "200", "color": "Negro"},
        {"modelo": "Aftershokz Aeropex", "marca": "Aftershokz", "tipo": "Bone conduction", "inalambrico": "Sí", "bateria": "8 horas", "cancelacion_ruido": "No", "precio": "160", "color": "Gris"},
        {"modelo": "Philips SHP9500", "marca": "Philips", "tipo": "Over-ear", "inalambrico": "No", "bateria": "N/A", "cancelacion_ruido": "No", "precio": "80", "color": "Negro"},
        {"modelo": "Plantronics BackBeat Go 600", "marca": "Plantronics", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "18 horas", "cancelacion_ruido": "No", "precio": "80", "color": "Azul"},
        {"modelo": "Bowers & Wilkins PX7", "marca": "Bowers & Wilkins", "tipo": "Over-ear", "inalambrico": "Sí", "bateria": "30 horas", "cancelacion_ruido": "Sí", "precio": "400", "color": "Gris"}
    ]
    
    # Agregar a la lista principal y guardar los datos
    audifonos.extend(audifonos_iniciales)
    guardar_datos()

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 8:
                    audifono = {
                        "marca": partes[0], "modelo": partes[1], "tipo": partes[2], "precio": partes[3],
                        "inalambrico": partes[4], "bateria": partes[5], "cancelacion_ruido": partes[6], "color": partes[7]
                    }
                    audifonos.append(audifono)

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for audifono in audifonos:
            f.write(f"{audifono['modelo']},{audifono['marca']},{audifono['tipo']},{audifono['inalambrico']},{audifono['bateria']},{audifono['cancelacion_ruido']},{audifono['precio']},{audifono['color']},\n")

def registrar_audifono():
    modelo = simpledialog.askstring("Registro", "Ingrese el modelo del audífono:")
    
    # Verificar si el modelo ya existe
    for audifono in audifonos:
        if audifono["modelo"] == modelo:
            messagebox.showwarning("Duplicado", "El modelo ya está registrado. Ingrese un modelo diferente.")
            return  # Salir de la función sin guardar

    # Si el modelo no existe, solicitar el resto de los datos
    datos = {"modelo": modelo}
    campos = ["marca", "tipo", "precio", "inalambrico", "bateria", "cancelacion_ruido", "color"]
    for campo in campos:
        datos[campo] = simpledialog.askstring("Registro", f"Ingrese {campo} del audífono:")
    
    audifonos.append(datos)
    guardar_datos()
    messagebox.showinfo("Éxito", "Audífono registrado exitosamente")

def consultar_audifono():
    modelo = simpledialog.askstring("Consulta", "Ingrese el modelo del audífono para consultar sus datos:")
    encontrado = False
    for audifono in audifonos:
        if audifono['modelo'] == modelo:
            encontrado = True
            info = "\n".join([f"{k.capitalize()}: {v}" for k, v in audifono.items()])
            messagebox.showinfo("Datos del audífono", info)
            break
    if not encontrado:
        messagebox.showwarning("No encontrado", f"No se encontró un audífono con el modelo {modelo}.")

def editar_audifono():
    modelo = simpledialog.askstring("Editar", "Ingrese el modelo del audífono para editar sus datos:")
    for audifono in audifonos:
        if audifono['modelo'] == modelo:
            for campo in ["marca", "tipo", "precio", "inalambrico", "bateria", "cancelacion_ruido", "color"]:
                nuevo_valor = simpledialog.askstring("Editar", f"Ingrese el nuevo {campo} o presione Enter para mantener el actual:")
                if nuevo_valor:
                    audifono[campo] = nuevo_valor
            guardar_datos()
            messagebox.showinfo("Éxito", "Audífono editado exitosamente.")
            return
    messagebox.showwarning("No encontrado", f"No se encontró un audífono con el modelo {modelo}.")

def eliminar_audifono():
    modelo = simpledialog.askstring("Eliminar", "Ingrese el modelo del audífono que desea eliminar:")
    for audifono in audifonos:
        if audifono['modelo'] == modelo:
            audifonos.remove(audifono)
            guardar_datos()
            messagebox.showinfo("Éxito", f"El audífono modelo {modelo} ha sido eliminado.")
            return
    messagebox.showwarning("No encontrado", f"No se encontró un audífono con el modelo {modelo}.")

def mostrar_tabla():
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("Tabla de Audífonos Registrados")
    ventana_tabla.geometry("800x400")

    columnas = ("marca", "modelo", "tipo", "precio", "inalambrico", "bateria", "cancelacion_ruido", "color")
    tabla = ttk.Treeview(ventana_tabla, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        tabla.column(col, width=100)

    for audifono in audifonos:
        valores = tuple(audifono.get(col, "") for col in columnas)
        if any(valores):  
            tabla.insert("", tk.END, values=valores)

    tabla.pack(expand=True, fill="both")
    ventana_tabla.mainloop()

def main():

    cargar_datos_iniciales()
    cargar_datos()
    
    ventanaprincipal = tk.Tk()
    ventanaprincipal.geometry("400x400")
    ventanaprincipal.title("Menú de Audífonos")

    etiqueta = tk.Label(ventanaprincipal, text="Gestión de Audífonos", font=("Arial", 16))
    etiqueta.pack(pady=10)

    botones = [
        ("Registrar Audífono", registrar_audifono),
        ("Editar Audífono", editar_audifono),
        ("Consultar Audífono", consultar_audifono),
        ("Eliminar Audífono", eliminar_audifono),
        ("Mostrar Tabla de Audífonos", mostrar_tabla),
        ("Salir", ventanaprincipal.quit)
    ]

    for texto, comando in botones:
        boton = tk.Button(ventanaprincipal, text=texto, command=comando, width=30, height=2)
        boton.pack(pady=5)

    ventanaprincipal.mainloop()

main()
