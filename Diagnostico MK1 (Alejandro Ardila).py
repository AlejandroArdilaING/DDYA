def main():
    print("Positivo, negativo o cero")
    num = int(input("Ingrese el numero: "))
    if num > 0:
        print("El numero es positivo")
        if ((num-1)+(num-2)==num):
            print("Es un numero FINBONACCI")
        if num%2 == 1:
            print("Es primo")
    elif num < 0:
        print("El numero es negativo")
        if ((num-1)+(num-2)==num):
            print("Es un numero FINBONACCI")
        if num%2 == 1:
            print("Es primo")
    elif num == 0:
        print("El numero es cero")
        if ((num-1)+(num-2)==num):
            print("Es un numero FINBONACCI")
        if num%2 == 1:
            print("Es primo")
main()
