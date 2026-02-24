def falta():
    l1= [1,2,3,4,5,6,7,8,9,10]
    l2= [1,2,3,4,5,6,7,8]

    c1= [1,2,3,4,5,6,8,9,10]
    c2= [1,2,3,4,6,7,8]

    for i in range(len(l1)):
        if c1[i]!= l1[i]:
            print("Faltante: ",c1[i])
    for i in range(len(l2)):
        if c2[i]!= l2[i]:
            print("Faltante: ",c2[i])
falta()
    
