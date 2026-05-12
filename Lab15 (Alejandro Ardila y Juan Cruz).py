# =====================================
# VARIABLES GLOBALES
# =====================================

INFINITO = float('inf')


# =====================================
# GRAFOS COMO DICCIONARIOS
# =====================================

# Grafo 1 - De la imagen 1
grafo_1 = {
    0: {2: 2, 1: 2},
    1: {2: 2, 3: 2},
    2: {1: 2, 3: 2, 4: 2},
    3: {2: 2, 4: 2},
    4: {}
}

# Grafo 2 - De la imagen 2
grafo_2 = {
    0: {1: 10},
    1: {2: 20, 3: 1},
    2: {4: 30},
    3: {},
    4: {}
}

# Grafo 3 - De la imagen 3
grafo_3 = {
    0: {1: 5, 2: 2},
    1: {3: 2, 2: 4},
    2: {4: 1},
    3: {5: 5},
    4: {5: 1},
    5: {}
}


# =====================================
# FUNCION DIJKSTRA
# =====================================

def dijkstra(grafo, inicio, fin):
    """
    Encuentra el camino minimo usando el algoritmo de Dijkstra
    grafo: diccionario de adyacencia
    inicio: nodo inicial
    fin: nodo final
    """

    # Inicializar distancias
    distancias = {}
    padres = {}
    visitados = set()

    for nodo in grafo:
        distancias[nodo] = INFINITO
        padres[nodo] = None

    distancias[inicio] = 0

    # Procesar todos los nodos
    for _ in range(len(grafo)):

        # Encontrar el nodo no visitado con menor distancia
        nodo_actual = None
        distancia_minima = INFINITO

        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < distancia_minima:
                nodo_actual = nodo
                distancia_minima = distancias[nodo]

        if nodo_actual is None:
            break

        visitados.add(nodo_actual)

        # Actualizar distancias de los vecinos
        for vecino in grafo[nodo_actual]:

            distancia_nueva = (
                distancias[nodo_actual] +
                grafo[nodo_actual][vecino]
            )

            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                padres[vecino] = nodo_actual

    # Reconstruir el camino
    camino = []
    nodo_actual = fin

    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = padres[nodo_actual]

    camino.reverse()

    return distancias[fin], camino, distancias


# =====================================
# FUNCION BELLMAN-FORD
# =====================================

def bellman_ford(grafo, inicio, fin):
    """
    Encuentra el camino minimo usando el algoritmo de Bellman-Ford
    grafo: diccionario de adyacencia
    inicio: nodo inicial
    fin: nodo final
    """

    # Inicializar distancias
    distancias = {}
    padres = {}

    for nodo in grafo:
        distancias[nodo] = INFINITO
        padres[nodo] = None

    distancias[inicio] = 0

    # Relajar aristas V-1 veces
    cantidad_nodos = len(grafo)

    for _ in range(cantidad_nodos - 1):
        for nodo in grafo:
            for vecino in grafo[nodo]:

                distancia_nueva = (
                    distancias[nodo] +
                    grafo[nodo][vecino]
                )

                if distancia_nueva < distancias[vecino]:
                    distancias[vecino] = distancia_nueva
                    padres[vecino] = nodo

    # Verificar ciclos negativos
    hay_ciclo_negativo = False

    for nodo in grafo:
        for vecino in grafo[nodo]:

            if (
                distancias[nodo] +
                grafo[nodo][vecino]
            ) < distancias[vecino]:

                hay_ciclo_negativo = True

    if hay_ciclo_negativo:
        return None, None, None

    # Reconstruir el camino
    camino = []
    nodo_actual = fin

    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = padres[nodo_actual]

    camino.reverse()

    return distancias[fin], camino, distancias


# =====================================
# FUNCION PARA MOSTRAR RESULTADOS
# =====================================

def mostrar_resultado(
    nombre_grafo,
    grafo,
    algoritmo_nombre,
    distancia,
    camino,
    distancias_todas
):
    """
    Muestra el resultado del algoritmo de forma clara
    """

    print("\n" + "=" * 60)
    print(f"  {nombre_grafo}")
    print("=" * 60)

    print(f"\nGrafo original:")

    for nodo in grafo:

        if grafo[nodo]:

            for vecino in grafo[nodo]:
                print(
                    f"  {nodo} "
                    f"--({grafo[nodo][vecino]})--> "
                    f"{vecino}"
                )

        else:
            print(f"  {nodo} (sin salidas)")

    print(f"\n\nAlgoritmo: {algoritmo_nombre}")
    print("Inicio: 0, Fin: (último nodo)")

    if distancia is None:
        print("\nError: Hay ciclos negativos")

    else:
        print(f"\nDistancia minima: {distancia}")
        print(f"Camino: {' -> '.join(map(str, camino))}")

    print(f"\nDistancias desde inicio a todos los nodos:")

    for nodo in sorted(distancias_todas.keys()):

        if distancias_todas[nodo] == INFINITO:
            print(f"  Nodo {nodo}: inf (no alcanzable)")

        else:
            print(f"  Nodo {nodo}: {distancias_todas[nodo]}")


# =====================================
# FUNCION MENU
# =====================================

def mostrar_menu():
    """
    Muestra el menu principal
    """

    print("\n")
    print("=" * 60)
    print("SOLUCION DEL EJERCICIO - GRAFOS DE CAMINO MINIMO")
    print("=" * 60)

    print("\nElige un ejercicio:\n")
    print("  1) Ejercicio 1 - Grafo 1")
    print("  2) Ejercicio 2 - Grafo 2")
    print("  3) Ejercicio 3 - Grafo 3")
    print("  4) Salir\n")


def ejecutar_ejercicio_1():
    """
    Ejecuta el ejercicio 1 con el Grafo 1
    """

    print("\n\n" + "=" * 60)
    print("  EJERCICIO 1 - GRAFO 1")
    print("=" * 60)

    # GRAFO 1 con Dijkstra
    distancia_1, camino_1, dist_todas_1 = dijkstra(grafo_1, 0, 4)

    mostrar_resultado(
        "GRAFO 1 - DIJKSTRA",
        grafo_1,
        "Dijkstra",
        distancia_1,
        camino_1,
        dist_todas_1
    )

    # GRAFO 1 con Bellman-Ford
    distancia_1_bf, camino_1_bf, dist_todas_1_bf = bellman_ford(
        grafo_1,
        0,
        4
    )

    mostrar_resultado(
        "GRAFO 1 - BELLMAN-FORD",
        grafo_1,
        "Bellman-Ford",
        distancia_1_bf,
        camino_1_bf,
        dist_todas_1_bf
    )


def ejecutar_ejercicio_2():
    """
    Ejecuta el ejercicio 2 con el Grafo 2
    """

    print("\n\n" + "=" * 60)
    print("  EJERCICIO 2 - GRAFO 2")
    print("=" * 60)

    # GRAFO 2 con Dijkstra
    distancia_2, camino_2, dist_todas_2 = dijkstra(grafo_2, 0, 4)

    mostrar_resultado(
        "GRAFO 2 - DIJKSTRA",
        grafo_2,
        "Dijkstra",
        distancia_2,
        camino_2,
        dist_todas_2
    )

    # GRAFO 2 con Bellman-Ford
    distancia_2_bf, camino_2_bf, dist_todas_2_bf = bellman_ford(
        grafo_2,
        0,
        4
    )

    mostrar_resultado(
        "GRAFO 2 - BELLMAN-FORD",
        grafo_2,
        "Bellman-Ford",
        distancia_2_bf,
        camino_2_bf,
        dist_todas_2_bf
    )


def ejecutar_ejercicio_3():
    """
    Ejecuta el ejercicio 3 con el Grafo 3
    """

    print("\n\n" + "=" * 60)
    print("  EJERCICIO 3 - GRAFO 3")
    print("=" * 60)

    # GRAFO 3 con Dijkstra
    distancia_3, camino_3, dist_todas_3 = dijkstra(grafo_3, 0, 5)

    mostrar_resultado(
        "GRAFO 3 - DIJKSTRA",
        grafo_3,
        "Dijkstra",
        distancia_3,
        camino_3,
        dist_todas_3
    )

    # GRAFO 3 con Bellman-Ford
    distancia_3_bf, camino_3_bf, dist_todas_3_bf = bellman_ford(
        grafo_3,
        0,
        5
    )

    mostrar_resultado(
        "GRAFO 3 - BELLMAN-FORD",
        grafo_3,
        "Bellman-Ford",
        distancia_3_bf,
        camino_3_bf,
        dist_todas_3_bf
    )


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

seguir = True

while seguir:

    mostrar_menu()

    opcion = input(
        "Ingresa tu opcion (1-4): "
    ).strip()

    if opcion == "1":
        ejecutar_ejercicio_1()

    elif opcion == "2":
        ejecutar_ejercicio_2()

    elif opcion == "3":
        ejecutar_ejercicio_3()

    elif opcion == "4":
        print("\n¡Hasta luego!\n")
        seguir = False

    else:
        print(
            "\nError: Opcion invalida. "
            "Por favor ingresa una opcion entre 1 y 4\n"
        )

    if seguir:
        input("Presiona ENTER para volver al menu...")
