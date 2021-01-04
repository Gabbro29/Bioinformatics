def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    patron=Pattern
    geno=Genome
    for posi in range(len(geno)):
        if geno[posi:posi+len(patron)]==patron:
            positions.append(posi)
    
    return positions
print(PatternMatching("ATAT","GATATATGCATATACTT"))

print(True and (False or False))