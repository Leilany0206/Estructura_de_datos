def division(lista, index_inicial, index_final):

    pivote = lista[index_final]

    izq_index  = index_inicial
    der_index = index_final - 1

    while izq_index <= der_index:

        # Busqueda a la izquierda de algo menor que el pivote
        while izq_index <= index_final and lista[izq_index] < pivote:
            izq_index += 1

        # Busqueda a la derecha de algo mayor que el pivote
        while der_index >= index_inicial and lista[der_index] >= pivote:
            der_index -= 1

        # Cambio de lugar de los elementos que se guardaron arriba, es decir, el menor por el mayor 
        if izq_index < der_index:
            lista[der_index], lista[izq_index] =\
                lista[izq_index], lista[der_index]

        # Se mueve el pivote al final del lado izquierdo (en medio) después de cada partición
        else:
            lista[index_final], lista[izq_index] = lista[izq_index], lista[index_final]
            print(f"Pivote: {pivote} lista: {lista}")

    return izq_index

def sublista(lista, index_inicial, index_final): # Esto maneja los index para hacer las sublistas en division

    if (index_inicial >= index_final): # lista de un solo elemento
        return

    pivote_index = division(lista, index_inicial, index_final) # Divide la lista en dos partes

    # Acomodo de cada sublista (izq y der)
    sublista(lista, index_inicial, pivote_index - 1)
    sublista(lista, pivote_index + 1, index_final)

def quick_sort(lista): 
    print(lista)
    sublista(lista, 0, len(lista) - 1)

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

quick_sort(conjunto)