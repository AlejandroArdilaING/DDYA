# SEMANA 1: Diagnóstico Mk1 -Descripción:

Diagnóstico Mk1 es un programa diseñado para analizar un número ingresado por el usuario y clasificarlo según su signo o si es cero.

El programa evalúa el número ingresado y lo clasifica en las siguientes categorías:

-Positivo, Negativo o Cero

-Fibonacci o No Fibonacci

-Primo o No Primo

Funcionamiento general:

Sin importar si el número es positivo, negativo o cero, el programa siempre ejecuta los procesos de verificación para determinar si el número pertenece a la sucesión de Fibonacci y si es un número primo. Adicionalmente, se identifica y muestra la naturaleza del signo del número.

Si el número cumple al menos una de las siguientes condiciones:

-Es Fibonacci

-Es Primo

Cumple ambas condiciones

el resultado correspondiente se mostrará al usuario. En caso contrario, dichas clasificaciones no se muestran.

Diagrama de flujo

El programa cuenta con un diagrama de flujo que representa la ruta lógica que sigue el sistema según las clasificaciones obtenidas. En este diagrama:

Cada ruta está diferenciada mediante colores distintos

Los colores permiten identificar de forma visual los procesos independientes y las decisiones tomadas durante la ejecución

Ruta lógica:

-El usuario ingresa un número

-Se determina si es positivo, negativo o cero

-Se evalúa si el número es Fibonacci o no Fibonacci

-Se evalúa si el número es primo o no primo

-Se muestran únicamente las clasificaciones relevantes al usuario

Finaliza el programa

# SEMANA 2:
Se analiza el caso de la clasificación de los estudiantes para saber que estudiantes aprobaron y cuales no, se debe realizar un programa en lenguaje de python para resolver este problema y que el resultado solo arroje los estudiantes reprobados

Procedimiento general: Se da una lista con los resultados de los estudiantes y su nombre, el programa debe de leer esta lista y guardar el nombre de los usuarios cuya nota asociada sea reprobatoria y crear una lista con estos nombres para mostrarlos textualmente al usuario al finalizar el programa.

El diagrama de flujo muestra la ruta exacta y resumida de que ruta adopta el programa al ser ejecutado y cual es el resultado final.

Ruta logica:

-Se añade la lista con el nombre y nota de los estudiantes -Lee la lista -Clasifica a el estudiante segun su nota asociada -Se crea una lista vacia -Se añade a la lista vacia el nombre de los estudiantes con calificacion reprobatoria -Se muestran los resultados de manera textual al usuario

Finaliza el programa

Archibos adjuntos:

-Descripción del problema -Requerimientos(Historias de usuario) -Diagramas de flujo -Análisis de complejidad

Ejercicios:

En la primera parte se trabaja con un listado de funciones matemáticas, las cuales se analizan para comparar su orden de crecimiento, incluyendo funciones logarítmicas, polinómicas, exponenciales y factoriales, con el fin de entender cómo crecen a medida que aumenta el tamaño de la entrada.

En la segunda parte se analiza la complejidad temporal de las funciones Mistery, Pesky y Prestiferous, donde se determina su complejidad usando la notación Big-O. En este punto se observa que la complejidad depende de la cantidad de ciclos anidados que tiene cada función.

En la tercera parte se implementa el algoritmo Insertion Sort en lenguaje Python, adaptado para ordenar una lista de números en orden descendente, y se muestra su ejecución mediante una función principal.

-Se evalúa si el número es primo o no primo

-Se muestran únicamente las clasificaciones relevantes al usuario

Finaliza el programa

# SEMANA 3:

Actualización del Programa de Estudiantes: Estrategia "Divide y Conquistarás"

Este proyecto actualiza el programa de los estudiantes utilizando la técnica de Divide y Conquistarás, realizando cambios significativos para mejorar su eficiencia. A continuación se detallan las modificaciones y análisis realizados:

-Cambios Principales:

La lista que anteriormente se encontraba dentro del programa ahora se divide a la mitad, resolviendo el programa en subproblemas más pequeños, lo que incrementa la eficiencia general.

Se realizó un análisis completo del programa para identificar posibles soluciones y optimizar su funcionamiento.

-Diagramas:

Diagrama de flujo: Muestra la ruta específica que sigue el programa desde su inicio hasta el fin de la ejecución, incluyendo los diferentes caminos según los procesos internos.

Diagrama de secuencia: Describe de manera detallada los procesos internos del programa desde la ejecución hasta la finalización.

Diagrama de uso: Presenta de forma simplificada las tareas más importantes y la interacción entre el sistema y el usuario, indicando quién realiza cada acción.

-Ejercicios y Análisis:

Se incluyen ejercicios encontrados en la Semana 3 de las diapositivas.

Se analizó el código y se aplicó el Teorema Maestro para determinar su complejidad, considerando su costo y número de ejecuciones (time).

Finaliza programa

# SEMANA 4:

## Actualización del Programa de Estudiantes

Este proyecto desarrolla y analiza el **Programa de Estudiantes**, cuyo objetivo es determinar qué estudiantes aprueban una materia según una nota mínima establecida.

Durante esta semana se trabajó en:

- Modelado del sistema mediante diagramas.
- Análisis formal de complejidad.
- Comparación entre enfoque lineal y estrategia Divide y Conquistarás.


## Descripción del Programa

El programa:

1. Recibe una lista de estudiantes con sus respectivas notas.
2. Define una nota mínima aprobatoria (ej. 3.0).
3. Recorre la lista.
4. Evalúa cada nota.
5. Genera una lista con los estudiantes aprobados.
6. Muestra el resultado final.


## Diagramas Realizados

### Diagrama de Flujo
Representa el proceso completo:
- Inicio
- Recorrido de la lista
- Evaluación condicional
- Agregar a lista de aprobados
- Fin

### Diagrama de Secuencia
Describe la interacción entre:
- Usuario
- Programa
- Evaluador
- Lista de aprobados

Incluye el ciclo que recorre cada estudiante y la condición de aprobación.

### Diagrama de Uso
Define claramente:
- Qué hace el usuario (ingresar datos, solicitar resultados).
- Qué hace el sistema (evaluar, procesar y generar lista final).
  

## Análisis de Complejidad

### Enfoque Implementado (Lineal)

El algoritmo recorre la lista una sola vez.

Función de tiempo:

T(n) = c1 + c2n

Complejidad temporal:
O(n)

Complejidad espacial:
O(n)

Mejor caso:
O(n)

Peor caso:
O(n)

Se realizaron gráficas del mejor y peor caso, mostrando crecimiento lineal.


## Aplicación de Divide y Conquistarás (Análisis Teórico)

Se planteó una versión alternativa donde:

- La lista se divide en dos mitades.
- Cada mitad se resuelve como subproblema.
- Se combinan los resultados.

Estructura general:

T(n) = 2T(n/2) + O(n)

Aplicando el Teorema Maestro:

a = 2  
b = 2  
f(n) = O(n)

Resultado:

T(n) = O(n log n)

Se concluye que para este problema específico, el enfoque lineal O(n) es más eficiente que aplicar Divide y Conquistarás.


## Conclusión

- El algoritmo implementado es óptimo para el problema.
- No requiere ciclos anidados.
- Su crecimiento es lineal.
- El análisis formal confirma su eficiencia.
- Se realizó modelado estructural y análisis matemático completo.


## Finaliza programa







