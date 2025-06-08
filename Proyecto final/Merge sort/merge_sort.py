def merge_sort(lista):

    if len(lista) <= 1: # lista de un solo elemento
        return lista 

    mitad = len(lista) / 2 # Regresa la mitad de número de elementos en la lista 
    # Mitades

    # ERROR AQUÍ
    izq  = lista[:int(mitad)]
    der = lista[int(mitad):]

    # Función recursiva, en cada lado se vuelve a hacer la separación y unión con orden (def union_orden)
    izq_sorted  = merge_sort(izq)
    der_sorted = merge_sort(der)

    return union_orden(izq_sorted, der_sorted)

def union_orden(uno, dos): # Uno = Lista izq, Dos = Lista der
    uno_index = 0 
    dos_index = 0
    lista_ordenada = []

    while uno_index < len(uno) and dos_index < len(dos): # While activo mientras ambas listas tengan elementos
        # Toma el indice menor de cada lista y con él hace comparación con la lista contraria 
        if uno[uno_index] <= dos[dos_index]:
            lista_ordenada.append(uno[uno_index])
            uno_index += 1
        else:
            lista_ordenada.append(dos[dos_index])
            dos_index += 1

    # Toma los elementos sobrantes que hayan quedado en una lista si ya no hay más elementos en la otra para comparar
    while uno_index < len(uno):
        lista_ordenada.append(uno[uno_index])
        uno_index += 1

    while dos_index < len(dos):
        lista_ordenada.append(dos[dos_index])
        dos_index += 1

    print(f"Izq: {uno} Der: {dos} Lista ordenada: {lista_ordenada}")
    return lista_ordenada

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

merge_sort(conjunto)