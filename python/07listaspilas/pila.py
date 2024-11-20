# Aqui vamos a crear toda la logica de programacion
def crear_pila ():
 return []

def apilar(pila, elemento):
    pila.append(elemento)
    
def esta_vacia(pila):
    return len(pila)==0
    
def desapilar(pila):
    if esta_vacia(pila):
        raise IndexError("Error: No se puede desapilar, la pila esta vacia")
    return pila.pop()

def cima(pila):
     if esta_vacia(pila):
        raise IndexError("La pila esta vacia")
     return pila[-1]

def tamaño(pila):
    return len(pila)

def mostrar_pila(pila):
     if esta_vacia(pila):
        raise IndexError("Erro: No se puede mostrar, la pila esta vacia")
     return f"pila actual, (pila)"