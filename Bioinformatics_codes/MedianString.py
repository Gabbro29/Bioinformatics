
import os
repo=os.getcwd()
def HammingDistance(p,q):
    counter=0

    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

def DistanceBetweenPatternAndStrings(Pattern,Dna):
    k=len(Pattern)
    distance=0
    for dnastring in Dna:
        ham_dist=float('inf')
        for i in range(len(dnastring)):
            kmer=dnastring[i:i+k]
            if len(kmer)==k:
                if ham_dist>HammingDistance(kmer,Pattern):
                    ham_dist=HammingDistance(kmer,Pattern)
        distance+=ham_dist
    return distance

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

def AllDnaStrings(k):
    All=list(Neighbors("A"*k,k))
    return All

def MedianString(Dna,k):
    distance=float('inf')
    median=""  
    Patterns=AllDnaStrings(k)
    for i in range(len(Patterns)):
        pattern=Patterns[i]
        if distance>DistanceBetweenPatternAndStrings(pattern,Dna):
            distance=DistanceBetweenPatternAndStrings(pattern,Dna)
            median=pattern
    return median

r=open(repo+"/texts/medians.txt",'r')
medians=r.readlines()
r.close()
for i in range(len(medians)):
    medians[i]=medians[i].strip()

k=int(medians[0])
Dna=medians[1:]
print(MedianString(Dna,k))