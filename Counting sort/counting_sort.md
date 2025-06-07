# Selection Sort

E**s un algoritmo de ordenamiento que toma un arreglo **A** de **n** elementos y los ordena de manera eficiente. Este algoritmo es particular porque **no utiliza comparaciones de claves** para ordenar**1**. En cambio, aprovecha el hecho de que los **n** elementos se encuentran en un **rango limitado**, típicamente de **{1, 2, ..., k}**

---

## Funcionamiento

**Contar cuántas veces aparece cada número**: Primero se revisa el arreglo original y se lleva un registro de cuántas veces aparece cada número. Por ejemplo, si hay tres "4", se anota que el número 4 aparece tres veces.

**Organizar la información**:  Luego, se usa esa cuenta para saber  **en qué orden deben colocarse los números** . Se suman las cantidades de los números menores para saber dónde empieza cada uno en el arreglo ordenado.

**Colocar cada número en su lugar**: Finalmente, se construye un nuevo arreglo ordenado usando esa información.

![Alt Text](https://miro.medium.com/v2/resize:fit:200/format:webp/1*8guImFhbPKA4Q9k84sNaaA.gif)

---

## Time Complexity

### Mejor caso (Best-case): O(n + k)

### Caso promedio (Average-case): O(n + k)

### Peor caso (Worst-case): O(n + k)

* No usa comparaciones, lo que le permite ser más rápido que algoritmos basados en comparación.
* Depende de `k`, el rango de los valores a ordenar. Si `k` es grande en comparación con `n`, el rendimiento baja.
* Es muy eficiente cuando los valores están en un rango pequeño.

---

## Consideraciones

* **Dependencia del rango (`K`)**: Si `K` es muy grande, puede volverse ineficiente en espacio y tiempo.
* **Espacio Auxiliar**: Usa un arreglo adicional de tamaño `K`.
* **Estabilidad**: Su versión estable es esencial para algoritmos como Radix Sort

---

## Comparación con otros algoritmos

* Se **requiere una versión estable** de Counting Sort para que Radix Sort funcione correctamente.

A diferencia de la mayoría de los algoritmos de ordenamiento tradicionales (como Selection Sort, Bubble Sort, Insertion Sort, Mergesort y Quicksort), Counting Sort no se basa en comparaciones de claves para ordenar un arreglo. Esto lo coloca en una categoría diferente y le permite romper la barrera de O(n log n).

* **Quick Sort y Merge Sort:** Counting Sort es más rápido en tiempo lineal cuando el rango de datos es pequeño, pero Quick y Merge Sort son más generales y funcionan con cualquier tipo de dato comparable.
* **Bubble Sort:** Counting Sort es mucho más eficiente, con complejidad O(n + k) frente a O(n²) de Bubble Sort, que es muy lento para grandes datos.
* **Insertion Sort:** Aunque Insertion Sort es bueno para datos casi ordenados, Counting Sort supera su rendimiento para datos enteros en rangos limitados.
* **Selection Sort:** Counting Sort es significativamente más rápido, especialmente para grandes conjuntos, mientras que Selection Sort siempre opera en O(n²).
* **Radix Sort:** Counting Sort es la base de Radix Sort. Radix Sort usa Counting Sort para ordenar dígito a dígito, extendiendo su uso a números con rangos grandes.
* **Heap Sort:** Counting Sort es más rápido para datos con rango limitado y enteros, pero Heap Sort funciona para cualquier tipo de dato con tiempo O(n log n) y sin restricciones de rango.

---

## Fuentes

* GeeksforGeeks, «Counting Sort Data Structures and Algorithms Tutorials»,  *GeeksforGeeks* , 30 de enero de 2025. **https://www.geeksforgeeks.org/counting-sort/**
* MIT,  *6.006 Intro to Algorithms Recitation 11: Counting Sort* . 2011. [En línea]. Disponible en: **https://courses.csail.mit.edu/6.006/spring11/rec/rec11.pdf**
