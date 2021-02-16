def HammingDistance(p,q):
    counter=0
    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

def ApproximatePatternMatching(Text, Pattern , d): # text secuancia Pattern genoma
    list_ini=[]
    for i in range(0,len(Pattern)-len(Text)+1):
        if HammingDistance(Text,Pattern[i:i+len(Text)]) <= d:
            list_ini.append(i)
    return list_ini

read=open("pm2.txt",'r')
given_sec=read.readlines()
#print(given_sec)
sec_right=[]
for i in given_sec:
    sec_right.append(i.strip("\n"))
#print(sec_right)

secuencia=sec_right[0]
genoma=sec_right[1]
d=int(sec_right[2])
resultado=ApproximatePatternMatching(secuencia, genoma, d)
print(*resultado,sep=" ")