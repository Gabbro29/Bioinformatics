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
    Patterns=[]
    freqMap={}
    n=len(Text)
    if n==k:
        ran=1
    else:
        ran=n-k
    for i in range(ran):
        Pattern=Text[i:i+k]
        Neighborhood=list(Neighbors(Pattern,d))
        limi=len(Neighborhood)-1
        if limi==0:
            limi=1
        for j in range(limi):
            neighbor=Neighborhood[j]
            try:
                freqMap[neighbor]=freqMap[neighbor]+1
            except KeyError:
                freqMap[neighbor]=1
    m=freqMap[max(freqMap, key=lambda k:freqMap[k])]
    for  k in freqMap:
        if freqMap[k]==m:
            Patterns.append(k)
    return Patterns

re=open(repo+"/texts/fwm.txt",'r')
fwm=re.readlines()
re.close
for i in range(len(fwm)):
    fwm[i]=fwm[i].strip()

text=fwm[0]
k=int(fwm[1][0])
d=int(fwm[1][2])
print("FWWM:",*FrequentWordWithMismatches(text,k,d))
