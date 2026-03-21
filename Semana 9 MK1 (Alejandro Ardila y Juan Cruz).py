# ========== Agregar nodo ==========
def add_nodo(grafo, nodo):
    if  nodo not in grafo:
        grafo[nodo] = []

# ========== Agregar conexiones ==========
def add_conexiones(grafo, nodo1, nodo2):
    grafo[nodo1].append(nodo2)
    grafo[nodo2].append(nodo1)

# ========== Mostrar lista adyacentes ==========
def mostrar_lista_ady(grafo):
    for clave, valor in grafo.items():
        print(f"{clave} -----> {valor}")

# ========== Recorrido BFS ==========
def bfs(grafo, inicio):
    visitados = []
    cola = []

    cola.append(inicio)

    print("\nRecorrido BFS:")

    while len(cola) > 0:
        nodo = cola.pop(0)

        if nodo not in visitados:
            print(nodo, end=" -> ")
            visitados.append(nodo)

            for vecino in grafo[nodo]:
                cola.append(vecino)

    print("FIN")

# ========== Menu ==========
def menu():
    grafo = {"A":["A", "B", "C"],
             "B":["A", "D", "E"],
             "C":["A", "F"],
             "D":["B"],
             "E":["B", "G"],
             "F":["C", "H"],
             "G":["E", "H"],
             "H":["F", "G"]}
    while True:
        print("\n" + "=" * 47)
        print("Menu rutas de bodegas")
        print("=" * 47)
        print("1. Agregar nodo.")
        print("2. Añadir conexiones a un nodo.")
        print("3. Mostrar lista adyacencia.")
        print("4. Busqueda BFS")
        print("5. Busqueda DFS")
        print("6. Salir")
        print("=" * 47)
        try:
            option = int(input("Eliga una opcion: "))

            if option == 1:
                nodo = input("Escriba la etiqueta del nodo como una letra:  ").upper()
                print(f"➕  Se agrega al grafo el nodo: {nodo}")
                add_nodo(grafo, nodo)

            elif option == 2:
                nodo1 = input("Escriba el nodo que quiere conectar: ").upper()
                nodo2 = input(f"A que nodo desea conectar {nodo1} ↔️: ").upper()
                add_conexiones(grafo, nodo1, nodo2)
            elif option == 3:
                print("=== Lista de adyacencia ===")
                mostrar_lista_ady(grafo)
            elif option == 4:
                bfs(grafo, "A")
            elif option == 5:
                print(5)
            elif option == 6:
                exit("FINALIZACIÓN")
        except:
            print("⚠️" + "  " + "Elija una opcion valida")
# ========== Parte principal ==========
if __name__ == "__main__":
    menu()
