
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        #print(Pattern)
        freq[Pattern] = 0
        for elem in range(len(Text)):
            if Text[elem:elem+k]==Pattern:
                freq[Pattern]+=1
    return freq

def FindClumps(Text,k,L,t):
    patterns=[]
    lentxt=len(Text)
    for i in range(lentxt-L):
        Window=Text[i:i+L]
        freqMap=FrequencyMap(Window,k)
        #print(freqMap)
        
        for key in freqMap:
            if freqMap[key]>=t:
                patterns.append(key)
    pattern_si=[]
    for elem in patterns:
        if elem not in pattern_si:
            pattern_si.append(elem)
    return pattern_si


r=open("Genome.txt",'r')
data1=r.readlines()
#print(data1)
dat=FindClumps(data1,9,500,4)
print(dat)
print(*dat,sep=" ")
r.close