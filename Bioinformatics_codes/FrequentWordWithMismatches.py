import os
repo=os.getcwd()

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

def FrequentWordWithMismatches(Text,k,d):
    pass