# Quick Sort

El algoritmo de ordenamiento **Quick Sort** es una de las técnicas más importantes y eficientes. Utiliza el paradigma de **"divide y vencerás"**, y se caracteriza por realizar el trabajo pesado **antes** de las llamadas recursivas, a diferencia de Merge Sort.

---

## Funcionamiento

- Quick Sort es un algoritmo **basado en comparaciones y recursivo**.
- Utiliza un **pivote** para dividir el array en dos sublistas:
  - Una con elementos **menores al pivote** (S1).
  - Otra con elementos **mayores o iguales** al pivote (S2).
- Se aplica recursivamente Quick Sort sobre S1 y S2.
- La combinación final **no requiere mezcla**, solo concatenación, ya que el pivote queda en su posición final.

![Alt Text](https://miro.medium.com/v2/resize:fit:560/format:webp/1*1OXQp3jbpyUJHYMX5rrJOQ.gif)

---

## Time Complexity

### Mejor caso (Best-case): O(n log n)

### Caso promedio (Average-case): O(n log n)

### Peor caso (Worst-case): O(n²)

- El peor caso ocurre cuando la partición divide el array de forma muy desequilibrada (por ejemplo, cuando está ya ordenado y se elige el primer elemento como pivote).
- Las comparaciones en el peor caso siguen la suma `n - 1 + n - 2 + ... + 1`, lo que da O(n²).

---

## Consideraciones

- **Elección del pivote** es crucial para su rendimiento:
  - Puede ser el primer, último, o un elemento aleatorio.
  - Idealmente debe dividir el array de forma balanceada.
- **Espacio auxiliar**: O(log n) promedio, O(n) en el peor caso (por la pila de llamadas recursivas).
- Aunque no siempre es estable, es **muy eficiente en la práctica**.

---

## Comparación con otros algoritmos

- **Merge Sort**: Tiene peor rendimiento en la práctica, pero mejor caso peor (O(n log n) garantizado).
- **Heap Sort**: También es O(n log n), pero no es estable y tiene rendimiento menos predecible.
- **Bubble, Insertion y Selection Sort**: O(n²), mucho más lentos.
- **Radix Sort**: Puede ser O(n) pero depende del tipo de datos y no usa comparaciones.

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII*. 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms*. 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
