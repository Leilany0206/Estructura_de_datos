# Algoritmo de Ordenamiento Heap Sort

Es una técnica de ordenamiento basada en comparaciones que utiliza una estructura de datos especial llamada **heap**. Es uno de los algoritmos que son fundamento para soluciones más rápidas y eficientes.

---

## Funcionamiento

- Heap Sort crea un **min-heap** o **max-heap** a partir de los datos de entrada.
- En un **heap**, el nodo raíz representa el **mínimo o máximo**, según el tipo de heap.
- Un **heap** es un **árbol binario completo**, donde todos los niveles están completamente llenos excepto tal vez el último, alineado a la izquierda.

El algoritmo opera en dos fases:

1. **Construcción del heap**: Se convierte el array en un heap (usualmente un **max-heap** para ordenar en orden ascendente).
2. **Extracción y ordenamiento**:
   - Se elimina el nodo raíz (máximo).
   - Se intercambia con el último elemento no ordenado.
   - Se aplica **heapify** para mantener la propiedad del heap.
   - Este proceso se repite hasta que todos los elementos están ordenados.

![Alt Text](https://miro.medium.com/v2/resize:fit:560/format:webp/1*t5B9NRgJKTxgZYsLhwU8Zg.gif)

---

## Time Complexity

La eficiencia de Heap Sort es consistente para todos los casos:

### Mejor caso (Best-case): O(n log n)

### Peor caso (Worst-case): O(n log n)

### Caso promedio (Average-case): O(n log n)

- Más eficiente que algoritmos como Bubble Sort o Insertion Sort.
- Utiliza comparaciones y reorganización basada en el heap.

---

## Consideraciones

- **Espacio auxiliar:** O(1), lo que significa que se puede implementar **in-place**.
- **Estabilidad:** No es un algoritmo estable (no mantiene el orden de elementos iguales).
- Se utiliza en contextos donde se requieren límites superiores de tiempo garantizados, como en el **kernel de Linux** o en sistemas embebidos.
- Aunque menos usado que Merge o Quick Sort, es muy útil para trabajar con **grandes volúmenes de datos**.

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII*. 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms*. 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
