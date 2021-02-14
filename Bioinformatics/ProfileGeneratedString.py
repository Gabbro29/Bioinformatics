import random

def Normalize(Probabilities):
    P=Probabilities
    normal={}
    #print(P.items())
    for k,v in Probabilities.items():
        #print(k,v) #k=valor de la biblioteca y v= valor que contiene los valores de la libreria
        #print(P.values)
        normal[k]=P[k]/sum(P.values())
    return normal
prob={'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}

def WeightedDie(Probabilities):
    P=Probabilities
    n=random.uniform(0,1)
    #print(Probabilities.items())
    for p,v in Probabilities.items():
        n-=v
        if n<=0:
            return(p)

def Pr(Text, Profile):
    pro=1
    for col in range(len(Profile['A'])):
        if Text[col]=='A':
            pro=pro*Profile['A'][col]
        elif Text[col]=='C':
            pro=pro*Profile['C'][col]
        elif Text[col]=='G':
            pro=pro*Profile['G'][col]
        elif Text[col]=='T':
            pro=pro*Profile['T'][col]
    return pro

def ProfileGeneratedString(Text, profile, k):
    n=len(Text)
    probabilities={}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]]=Pr(Text[i:i+k],profile)
    probabilities=Normalize(probabilities)
    return WeightedDie(probabilities)