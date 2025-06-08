# Bubble Sort

Es una técnica fundamental para organizar una colección de elementos en **orden ascendente o descendente**. Es uno de los métodos de ordenamiento más simples y sirve como base para algoritmos más rápidos y eficientes.

Video recomendado: https://www.youtube.com/watch?v=lyZQPjUT5B4

---

## Funcionamiento

- El algoritmo recorre la lista comparando elementos adyacentes e **intercambiándolos si están en el orden incorrecto**.
- En cada pasada, los elementos más grandes se "burbujean" hacia el final (en orden ascendente) o hacia el principio (en orden descendente).
- Después de cada pasada, uno de los elementos ya está en su posición final y no se vuelve a comparar.
- El proceso se repite hasta que la lista está completamente ordenada o no se hacen intercambios en una pasada.

![Alt Text](https://miro.medium.com/v2/resize:fit:600/format:webp/1*1MiLjMYgr2r2fDORCJn89w.gif)

---

## Time Complexity

- La complejidad de tiempo del algoritmo Bubble Sort **depende no solo del tamaño de la lista, sino también del contenido inicial** de la misma.

### Mejor caso (Best-case): O(n)

- Ocurre cuando la lista ya está ordenada en orden ascendente.
- No se realizan intercambios, solo se hacen comparaciones.
- El número de comparaciones de claves es `n-1`, y el número de movimientos es 0.

### Peor caso (Worst-case): O(n²)

- Ocurre cuando la lista está en orden inverso (por ejemplo, descendente si se busca un orden ascendente).
- Se realizan muchas comparaciones e intercambios, con `n*(n-1)/2` comparaciones y un número similar de intercambios.

### Caso promedio (Average-case): O(n²)

- Para la mayoría de los casos de entrada "promedio", el rendimiento del algoritmo de burbuja también es O(n²).
- En general, el Bubble Sort se clasifica como un **algoritmo de tiempo cuadrático O(n²)**. Esto significa que su tiempo de ejecución crece rápidamente con el tamaño de los datos.

---

## Consideraciones

- Es un algoritmo de ordenamiento **simple y apropiado para entradas pequeñas**.
- Aunque en el peor de los casos su comportamiento es O(n²), en el mejor caso es O(n), lo que lo hace eficiente para listas casi ordenadas si se implementa una versión optimizada.
- La complejidad de tiempo es una medida importante para determinar qué algoritmo es más adecuado para un tipo particular de datos y aplicación, especialmente cuando se trabaja con grandes volúmenes de datos.

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII* . 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms* . 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
