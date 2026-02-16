def estudiantes():

txt = ["Ana 4.5, Juan 3.2, Maria 4.0"]

estudiantes = txt.split(",")

sum_not = 0
total_estu = 0

for estudiante in estudiantes:
    datos = estudiante.split(" ")
    nota = float(datos[1])
    sum_not = sum_not + nota
    total_estu = total_estu + 1

promedio = sum_not / total_estu

print("Promedio:", promedio)
print("Estudiantes por encima del promedio:")

for estudiante in estudiantes:
    datos = estudiante.split(" ")
    nombre = datos[0]
    nota = float(datos[1])
    if nota > promedio:
        print(nombre)
estudiantes()
