import tkinter as tk
from tkinter import messagebox
from time import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



def sort_numbers():
    try:
        numbers = list(map(int, entry_numbers.get().split(',')))
        if len(numbers) > 40:
            messagebox.showerror("Error", "El máximo de números permitido es 40.")
            return

        method = sort_method.get()
        if not method:
            messagebox.showerror("Error", "Selecciona un método de ordenamiento.")
            return

        original = numbers.copy()
        start_time = time()

        if method == "Método Burbuja":
            sorted_numbers = bubble_sort(numbers)
        elif method == "Insertion Sort":
            sorted_numbers = insertion_sort(numbers)
        elif method == "Selection Sort":
            sorted_numbers = selection_sort(numbers)
        elif method == "Merge Sort":
            sorted_numbers = merge_sort(numbers)
        elif method == "Quick Sort":
            sorted_numbers = quick_sort(numbers)
        else:
            messagebox.showerror("Error", "Método de ordenamiento no válido.")
            return

        end_time = time()
        elapsed_time = end_time - start_time

        messagebox.showinfo(
            "Resultados",
            f"Lista Original: {original}\n"
            f"Lista Ordenada: {sorted_numbers}\n"
            f"Tiempo de Ejecución: {elapsed_time:.6f} segundos"
        )
    except ValueError:
        messagebox.showerror("Error", "Asegúrate de ingresar una lista de números separados por comas.")


# Interfaz gráfica
root = tk.Tk()
root.title("Ordenamiento de Números")

tk.Label(root, text="Ingrese una lista de números (máximo 40), separados por comas:").pack(pady=10)
entry_numbers = tk.Entry(root, width=50)
entry_numbers.pack(pady=5)

tk.Label(root, text="Selecciona un método de ordenamiento:").pack(pady=10)

sort_method = tk.StringVar(value=None)
tk.Radiobutton(root, text="Método Burbuja", variable=sort_method, value="Método Burbuja").pack(anchor='w')
tk.Radiobutton(root, text="Insertion Sort", variable=sort_method, value="Insertion Sort").pack(anchor='w')
tk.Radiobutton(root, text="Selection Sort", variable=sort_method, value="Selection Sort").pack(anchor='w')
tk.Radiobutton(root, text="Merge Sort", variable=sort_method, value="Merge Sort").pack(anchor='w')
tk.Radiobutton(root, text="Quick Sort", variable=sort_method, value="Quick Sort").pack(anchor='w')

tk.Button(root, text="Ordenar", command=sort_numbers).pack(pady=20)

root.mainloop()