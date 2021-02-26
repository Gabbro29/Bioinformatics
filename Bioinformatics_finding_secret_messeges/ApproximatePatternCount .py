import os
direct=os.getcwd()

def HammingDistance(p,q):
    counter=0

    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

def ApproximatePatternCount(Pattern, Text,d): #pattern == secuencia ,,, Text== genoma ,,, d diferencia
    count = 0 

    for i in range(len(Text)):
        owo=Text[i:i+len(Pattern)]
        if len(owo)==len(Pattern):
            #print(owo)
            if HammingDistance(owo, Pattern)<=d:
                count+=1    
    return count

r=open(direct+"/texts/apc.txt",'r')
inp=r.readlines()
for j in range(len(inp)):
    inp[j]=inp[j].strip("\n")
secuencia=inp[0]
genoma=inp[1]
diferencia=int(inp[2])
print("ApproxPatternCount:",ApproximatePatternCount(secuencia,genoma,diferencia))
r.close()