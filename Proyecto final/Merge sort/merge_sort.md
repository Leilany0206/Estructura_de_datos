# Algoritmo de Ordenamiento Merge Sort

Es una técnica fundamental y altamente eficiente, conocida por su consistencia en el rendimiento. Junto con Quick Sort, es uno de los algoritmos clave basados en el paradigma de **"divide y vencerás"**.

---

## Funcionamiento

- Merge Sort es un algoritmo de **comparación recursivo**.
- Aplica el enfoque **"divide y vencerás"** para dividir la lista en sublistas, ordenarlas y luego fusionarlas.
- Funciona en tres fases principales:

1. **Dividir**: El array se divide repetidamente en mitades hasta obtener sublistas de un solo elemento.
2. **Ordenar**: Cada sublista se ordena de forma recursiva mediante llamadas al mismo algoritmo.
3. **Mezclar**: Se fusionan las sublistas ordenadas en un **array temporal**, que luego se copia al array original.

![Alt Text](https://miro.medium.com/v2/resize:fit:600/format:webp/1*opwN0BhtH4zvPF697fPlow.gif)

---

## Time Complexity

### Mejor caso (Best-case): O(n log n)

### Peor caso (Worst-case): O(n log n)

### Caso promedio (Average-case): O(n log n)

- La cantidad de comparaciones de claves en el peor caso es aproximadamente `n * log2n - n - 1`.
- En la etapa de fusión, combinar dos arrays ordenados de tamaño `k` implica hasta `2k - 1` comparaciones.

---

## Consideraciones

- **Espacio auxiliar:** O(n). Requiere un array adicional del mismo tamaño que el original.
- **Estabilidad:** Sí. Mantiene el orden relativo de los elementos iguales.
- Muy eficiente para **grandes volúmenes de datos**.
- En listas enlazadas, la memoria auxiliar puede reducirse pero requiere tiempo para dividir.

---

## Comparación con otros algoritmos

- **Bubble, Selection e Insertion Sort**: O(n²) → menos eficientes.
- **Heap Sort**: Igual de eficiente en complejidad (O(n log n)) pero no es estable.
- **Quick Sort**: O(n log n) promedio, pero puede degradarse a O(n²) en el peor caso.
- **Radix Sort**: Puede ser O(n), pero depende de características específicas de los datos y no usa comparaciones.

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII*. 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms*. 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
