# Selection Sort

Es un algoritmo sencillo de implementar que organiza una lista seleccionando repetidamente el elemento más pequeño (o más grande, si es descendente) y colocándolo en su posición correcta. Este proceso se repite hasta que toda la lista está ordenada.

Video recomendado: https://www.youtube.com/watch?v=Ns4TPTC8

---

## Funcionamiento

* **Dividir en dos partes**: La lista se divide en una **parte ordenada** (al principio vacía) y una **parte no ordenada** (que contiene todos los elementos inicialmente).
* **Buscar el mínimo**: En cada paso, se **recorre la parte no ordenada** para  **encontrar el elemento más pequeño** .
* **Intercambiar**: Una vez que se encuentra el elemento más pequeño, se  **intercambia con el primer elemento de la parte no ordenada** . Así, ese elemento queda en su posición definitiva en la parte ordenada.
* **Mover la frontera:** La "pared imaginaria" entre la parte ordenada y la no ordenada **avanza una posición** hacia la derecha.
* **Repetir:** Se repite el proceso con el resto de la lista no ordenada, buscando el siguiente más pequeño e intercambiándolo con el primer elemento de esa parte. Esto se repite hasta que solo queda un elemento en la parte no ordenada, que ya estará en su lugar.

![Alt Text](https://miro.medium.com/v2/resize:fit:200/format:webp/1*8guImFhbPKA4Q9k84sNaaA.gif)

---

## Time Complexity

### Mejor caso (Best-case): O(n²)

### Caso promedio (Average-case): O(n²)

### Peor caso (Worst-case): O(n²)

* El número de comparaciones siempre es el mismo: `n(n - 1) / 2`.
* La cantidad de intercambios es menor que otros algoritmos simples, como Bubble Sort.

---

## Consideraciones

* **No requiere memoria adicional** (espacio auxiliar O(1)).
* **No es estable** : los elementos con el mismo valor pueden cambiar su orden relativo.
* Es adecuado solo para **arreglos pequeños** o cuando el costo de intercambio es muy alto, ya que realiza pocos intercambios.
* **Fácil de implementar** y entender.

---

## Comparación con otros algoritmos

* **Quick Sort** y  **Merge Sort** : Mucho más rápidos (O(n log n)).
* **Bubble Sort** : Similar en tiempo, pero generalmente más lento en la práctica.
* **Insertion Sort** : Más eficiente que Selection Sort en casos parcialmente ordenados.
* **Heap Sort** : Más eficiente, también basado en comparaciones y sin estabilidad.
* **Radix Sort** : Puede ser más rápido, pero solo con ciertos tipos de datos (enteros o cadenas con longitud fija).

---

## Fuentes

* NCERT,  *Computer Science Textbook for Class XII*. 2020. [Ebook]. Disponible en: **https://ncert.nic.in/textbook/pdf/lecs105.pdf#page=1.58**
* CENG 707 Data Structures and Algorithms,  *Sorting algorithms*. 2016. [En línea]. Disponible en: **https://user.ceng.metu.edu.tr/~tcan/ceng301_s1516/Schedule/week4.pdf**
* J. Long, “Understanding Sorting Algorithms - JL Codes - Medium,”  *Medium*, 2018.[En línea]. Disponible en:**https://medium.com/jl-codes/understanding-sorting-algorithms-af6222995c8**
