def HammingDistance(p,q):
    counter=0

    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

def ApproximatePatternMatching(Text, Pattern , d): # text secuancia Pattern genoma
    list_ini=[]
    for i in range(len(Pattern)):
        uwu=Pattern[i:i+len(Text)]
        if len(uwu)==len(Text):
            #print(uwu, Text)
            if HammingDistance(uwu,Text) <= d:
            
                list_ini.append(i)
    return list_ini

print(ApproximatePatternMatching("ATTCTGGA","CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT",3))