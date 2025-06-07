# Insertion Sort

Es una técnica de ordenamiento que permite organizar una colección de elementos en **orden ascendente o descendente**. Es una de las metodologías de ordenamiento fundamentales, sirviendo de base para algoritmos más rápidos y eficientes.

---

## Funcionamiento

- El algoritmo recorre la lista a partir del segundo elemento (índice 1, asumiendo que el primer elemento, índice 0, ya está en la "lista ordenada" por sí mismo).
- Para cada elemento `pivote` de la parte no ordenada (comenzando desde el segundo elemento), se compara con los elementos de la lista ordenada, **recorriéndolos hacia atrás**.
- Si un elemento en la parte ordenada es mayor que `pivote`, se **desplaza una posición a la derecha** para hacer espacio.
- Este desplazamiento continúa hasta que se encuentra una posición donde `pivote` es mayor o igual que el elemento anterior, o hasta que se llega al principio de la lista ordenada.
- Finalmente, `pivote` se inserta en esa posición.
- Este proceso se repite hasta que todos los elementos de la lista no ordenada han sido insertados en la lista ordenada, lo que resulta en una lista completamente ordenada.

  ![Alt Text](https://miro.medium.com/v2/resize:fit:600/format:webp/1*bmfRxyIQZEK0Iu5T6YV1sw.gif)

---

## Time Complexity

- La complejidad de tiempo del algoritmo de ordenamiento por inserción **depende no solo del tamaño de la lista, sino también del contenido inicial** de la misma.

### Mejor caso (Best-case): O(n)

- Ocurre cuando la lista ya está ordenada en orden ascendente.
- En este escenario, el bucle interno prácticamente no se ejecuta, ya que no se necesitan desplazamientos.
- El número de comparaciones de claves es `n-1`, y el número de movimientos es `2*(n-1)`.

### Peor caso (Worst-case): O(n²)

- Ocurre cuando la lista está en orden inverso (por ejemplo, ordenada descendentemente si se busca un orden ascendente).
- El bucle interno se ejecuta un número máximo de veces, lo que lleva a `n*(n-1)/2` comparaciones de claves y `2*(n-1) + n*(n-1)/2` movimientos.

### Caso promedio (Average-case): O(n²)

- Para la mayoría de los casos de entrada "promedio", el rendimiento del algoritmo por inserción también es O(n²).
- En general, el ordenamiento por inserción se clasifica como un **algoritmo de tiempo cuadrático O(n²)**. Esto significa que su tiempo de ejecución crece rápidamente con el tamaño de los datos.

---

## Consideraciones

- Es un algoritmo de ordenamiento **simple y apropiado para entradas pequeñas**.
- Aunque en el peor de los casos su comportamiento es O(n²), en el mejor caso es O(n), lo que lo hace eficiente para listas casi ordenadas.
- La complejidad de tiempo es una medida importante para determinar qué algoritmo es más adecuado para un tipo particular de datos y aplicación, especialmente cuando se trabaja con grandes volúmenes de datos.

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII* . 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms* . 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
