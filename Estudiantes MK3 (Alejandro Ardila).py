def estudiantes():

    lista = ["Ana 4.5", "Juan 3.2", "Maria 4.0", "Luis 2.0"]
    aprobados = []

    n = len(lista)
    tamaño = n

    while tamaño >= 1:

        inicio = 0

        while inicio < n:

            fin = inicio + tamaño

            if fin <= n:

                if tamaño == 1:

                    datos = lista[inicio].split(" ")
                    nombre = datos[0]
                    nota = float(datos[1])

                    if nota >= 3:
                        aprobados.append(nombre)

            inicio = inicio + tamaño

        tamaño = tamaño // 2

    print("Lista de estudiantes que aprobaron:")
    print(aprobados)


estudiantes()

