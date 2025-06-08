def selection_sort(lista):

    for i in range(len(lista)):

        menor = i # Guarda el index del número menor  
        for j in range(i + 1, len(lista)): # Iteración que empieza un indice arriba del que sería nuestro pivote
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i] # Intercambio de valores, el pivote por el menor 

        print(f"Paso {i}: {lista} Pivote actual: {lista[i]}")

conjunto = [4, 9, 8, 3, 1, 0, 2, 0]

selection_sort(conjunto)