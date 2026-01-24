def main():
    estudiantes = []
    pasaron = []
    nombre = input("Nombre de alumno y su calificacion: ")
    estudiantes = nombre.split(" ")
    for j in range(0,len(estudiantes),2):
        if j >= 3:
            pasaron = pasaron.append(estudiantes[j-1])

    print(pasaron)
main()
        
        
                 
    
