import os
repo=os.getcwd()

def HammingDistance(p,q):
    counter=0

    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

def Neighbors(Pattern,d):
    if d==0:
        return {Pattern}
    if len(Pattern)==1:
        return {"A","C","G","T"}
    Neighborhood=set()
    SuffixNeighbors=Neighbors(Pattern[1:],d)
    for text in SuffixNeighbors:
        if HammingDistance(text,Pattern[1:])<d:
            for nucleotide in ["A","G","T","C"]:
                Neighborhood.add(nucleotide+text)
        else:
            Neighborhood.add(Pattern[0]+text)
    return Neighborhood

te=open(repo+"/texts/nboor.txt",'r')
inpu=te.readlines()
te.close()
for i in range(len(inpu)):
    inpu[i]=inpu[i].strip("\n")
pattern=inpu[0]
distance=int(inpu[1])
print("Neighbors:",*Neighbors(pattern,distance))