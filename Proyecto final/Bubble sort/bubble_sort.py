def bubble_sort(lista):
    print(lista)
    x = len(lista)

    for i in range(x): # Recorre los elementos de la lista
        for j in range(x-1-i): # Recorre con cada iteración un dos index menos
            # Compara un index y su siguiente, para al comparar con último sin ordenar
            print(f"Elementos comparados: {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j+1]: # Si es mayor, los cambia
                lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

bubble_sort(conjunto)