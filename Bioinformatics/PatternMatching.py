def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    patron=Pattern
    geno=Genome
    for posi in range(len(geno)):
        if geno[posi:posi+len(patron)]==patron:
            positions.append(posi)
    return positions
r=open("Vibrio_cholerae.txt",'r')
data1=str(r.readlines())
#print(type(data1))
data=PatternMatching("CTTGATCAT",data1)
print(*data,sep=" ")


r.close()
