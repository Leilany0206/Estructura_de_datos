def counting_sort(lista, max):

    # Se genera una lista con n+1 posiciones más que el valor más grande de la lista 
    conteo = list(0 for _ in range(max + 1))
    # Conteo de veces que aparece un número, este coincide al index
    for item in lista:
        conteo[item] += 1

    print(f"Lista: {lista}")
    print(f"Frecuencia de cada número: { {i: v for i, v in enumerate(conteo)} }")


    conteo_previo = 0 # Para iniciar el conteo
    for i, frecuencia in enumerate(conteo): # i = index, frecuencia = valor guardado en ese index
        
        # En cada iteración guarda el conteo acumulado, ya no la frecuencia de cada num por separado
        conteo[i] = conteo_previo 
        conteo_previo += frecuencia 

    print(f"Frecuencia acumulada: { {i: v for i, v in enumerate(conteo)} }")

    # Lista vacia para los valores ordenados
    lista_ordenada = [None] * len(lista)

    for item in lista:

        # El value en lista con indice 0, 1, 2... sucesivamente indica el index de conteo, este a su vez, indica el index en lista ordenada
        lista_ordenada[conteo[item]] = item

        # Aumenta en 1 la posición de ese número en conteo, para que si aparece otra vez, se coloque después del anterior
        conteo[item] += 1

    print(f"Lista ordenada: {lista_ordenada}")
    return lista_ordenada

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

counting_sort(conjunto, 9)