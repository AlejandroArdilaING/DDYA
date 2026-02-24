def minimo():
    n1 = [2,1,2,3,4]
    n2 = [8,5,4,3,4,10]

    tam1 = len(n1)
    tam2 = len(n2)
    men1 = 10
    men2 = 10

    for i in range (tam1):
        if n1[i]< men1:
            men1 = n1[i]
    print("Menor en lista 1: ",men1)
    for i in range (tam2):
        if n2[i]< men2:
            men2 = n2[i]
    print("Menor en lista 2: ",men2)
    
minimo()
    
