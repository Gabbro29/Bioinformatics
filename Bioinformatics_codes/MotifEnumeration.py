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

def ApproximatePatternMatching(Text, Pattern , d): # text secuancia Pattern genoma
    list_ini=[]
    for i in range(0,len(Pattern)-len(Text)+1):
        if HammingDistance(Text,Pattern[i:i+len(Text)]) <= d:
            list_ini.append(i)
    return list_ini

def MotifEnumeration(Dna, k, d):
    patterns=set()
    for i in range(len(Dna[0])):
        if i+k<=len(Dna[0]):
            kmer=Dna[0][i:i+k]
            #print(kmer)
            similarkmer=list(Neighbors(kmer,d))
            #print(similarkmer)
            for skmer in similarkmer:
                skmer_count=0
                for dnastring in Dna:
                    if len(ApproximatePatternMatching(skmer, dnastring,d))>=1:
                        skmer_count+=1
                if skmer_count==len(Dna):
                    patterns.add(skmer)
    return patterns




r=open(repo+"/texts/motifenu.txt",'r')
motifenu=r.readlines()
r.close()
for i in range(len(motifenu)):
    motifenu[i]=motifenu[i].strip()
k=int(motifenu[0][0])
d=int(motifenu[0][2])
dna=list(motifenu[1:len(motifenu)])

print(*MotifEnumeration(dna,k,d))