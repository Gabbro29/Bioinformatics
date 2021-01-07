def Normalize(Probabilities):
    P=Probabilities
    normal={}
    #print(P.items())
    for k,v in Probabilities.items():
        #print(k,v) #k=valor de la biblioteca y v= valor que contiene los valores de la libreria
        #print(P.values)
        normal[k]=P[k]/sum(P.values())
    return normal
prob={'A': 0.22, 'C': 0.54, 'G': 0.36, 'T': 0.3}

print(Normalize(prob))