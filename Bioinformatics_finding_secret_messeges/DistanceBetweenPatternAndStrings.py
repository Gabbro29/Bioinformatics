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

r=open(repo+"/texts/dps.txt","r")
dps=r.readlines()
r.close()
for i in range(len(dps)):
    dps[i]=dps[i].strip()
Pattern=dps[0]
Dna=dps[1].split(" ")

print(DistanceBetweenPatternAndStrings(Pattern,Dna))

