import tkinter as tk
from tkinter import messagebox
def crear_interfaz(logica_cola):
    ventana = tk.Tk()
    ventana.title("Ejempko de una cola sencilla")
    ventana.geometry("400x400")
    # defibnimos cola
    cola = logica_cola["crear_cola"]()
    
    def manejar_encolar():
        elemento = entrada_elemento.get()
        if elemento:
            logica_cola["encolar"](cola, elemento)
            actualizar_colar()
            entrada_elemento.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacia. Por favor ingrese un elemento")

    def manejar_desencolar():
        try:
            elemento = logica_cola["desencolar"](cola)
            messagebox.showinfo("desencolar", f"elemento desencolado:{elemento}")(cola)
            actualizar_cola()
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def manejar_frente():
        try:
            elemento = logica_cola["frente"](cola)
            messagebox.showinfo("frente", f"elemento al frente de la cola es:{elemento}")(cola)
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def manejar_tamaño():
        tam = logica_cola["tamaño"](cola)
        messagebox.showinfo("tamaño: ", f"El tamaño de la cola es: {tam}")
    
    def manejar_mostrar():
        cola_actual = logica_cola["mostrar_cola"](cola)
        messagebox.showinfo("cola actual:", cola_actual)
    
    def actualizar_cola():
        cola_actual = logica_cola["mostrar_cola"](cola)
        etiqueta_cola.config(text=cola_actual)
        
