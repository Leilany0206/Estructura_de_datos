def heapify(lista, n, i): # Lista, tamaño del heap, index del nodo a ajustar
    mayor = i  # Nodo más grande / raíz

    # Calcula la posición de cada nodo en la lista
    izq = 2 * i + 1  
    der = 2 * i + 2  

    # Compara nodo izq y nodo actual, si es mayor, izq se convierte en mayor
    if izq < n and lista[i] < lista[izq]:
        mayor = izq

    # Compara nodo der y nodo actual, si es mayor, der se convierte en mayor
    if der < n and lista[mayor] < lista[der]:
        mayor = der

    # Si el nodo más grande no es el nodo actual (n), se intercambian 
    if mayor != i:
        (lista[i], lista[mayor]) = (lista[mayor], lista[i]) 
        heapify(lista, n, mayor) # Llamada recursiva

    print(lista)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2, -1, -1): # n // 2 es el index del último nodo padre
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1): # n - 1 empieza en el último index
        # Se pone el último valor al inicio (nodo raíz y mayor) para hacer la comparación
        lista[i], lista[0] = lista[0], lista[i]  
        heapify(lista, i, 0)

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

heap_sort(conjunto)