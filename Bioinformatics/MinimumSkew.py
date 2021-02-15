def SkewArray(Genome):
    Skew={}
    for i in range(len(Genome)):
        if i == 0:
            Skew[0]=0
        if Genome[i]=="A" or Genome[i]=="T":
            Skew[i+1]= Skew[i]
        if Genome[i]=="G":
            Skew[i+1]=Skew[i]+1
        if Genome[i]=="C":
            Skew[i+1]=Skew[i]-1
    ske=[]
    for i in range(len(Skew)):
        ske.append(Skew[i])
    return ske

def MinimumSkew(Genome):
    skew=SkewArray(Genome)
    posis=[]
    minimo=min(skew)
    

    for i in range(len(skew)):
        if skew[i]==minimo:
            posis.append(i)
    return posis
r=open("Text_skew.txt",'r')
Geno_test=r.readlines()
#Geno=input("Genome:")
print("Position of minimum skew:", MinimumSkew(Geno_test))