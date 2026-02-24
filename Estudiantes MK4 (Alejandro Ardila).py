
nota_minima_para_aprobar = 3.0

lista_estudiantes = ["Ana",4.5,"Luis",2.8,"Carlos",3.2,"Maria",2.5,"Pedro",3.0]

resultados_guardados = {}
lista_aprobados = []

def revisar_nota(nombre_estudiante, nota_estudiante):
    
    if nombre_estudiante in resultados_guardados:
        return resultados_guardados[nombre_estudiante]
    
    if nota_estudiante >= nota_minima_para_aprobar:
        estado = "aprobado"
    else:
        estado = "reprobado"
    
    resultados_guardados[nombre_estudiante] = estado
    
    return estado


for i in range(0, len(lista_estudiantes), 2):
    
    nombre = lista_estudiantes[i]
    nota = lista_estudiantes[i + 1]
    
    resultado_final = revisar_nota(nombre, nota)
    
    if resultado_final == "aprobado":
        lista_aprobados.append(nombre)


print(lista_aprobados)
