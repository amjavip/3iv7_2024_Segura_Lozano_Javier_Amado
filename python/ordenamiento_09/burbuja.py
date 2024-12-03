#burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-1-i):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#metodo sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range (i+1, n):
            if(lista[j] < lista[min_idx]):
                min_idx = j
                lista[i], lista[min_idx] = lista[min_idx], lista[i]       
# metodo de insercion
def  insercion(lista):
    for i in range (1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j = 1
            lista[j+1] = key 
    return lista

def marge(lista):
    if(len(lista)>1):
        mid = len(lista)//2
        izquierda = lista[:mid]
        derecha = lista[mid:]
        #recursivo
        marge(izquierda)
        marge(derecha)
        
        1 = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[i]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[k]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += i
        while i < len(derecha):
            lista[k] = derecha[i]
            i += 1
#quick sort
def quick_sort(lista):
    if(len(lista) <= 1):
        return lista
    pivote = lista[len(lista)//2]
    
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)
#tarea interfaz donde puede seleccionar algun metodo de ordenamiento y dar una lista con maximo de 40 elementos,   y de output de la lista original, la lista ordenada y cuanto tiempo tardo