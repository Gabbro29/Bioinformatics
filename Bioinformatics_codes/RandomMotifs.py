import random
 
def RandomMotifs(Dna, k, t):
    cant_nucl=len(Dna[0])
    random_motifs=[]
    for dna_string in Dna:
        ran_po=random.randint(0,cant_nucl-k)
        random_motifs.append(dna_string[ran_po:k+ran_po])
    return random_motifs

k=3
t=5
Dna=['TTACCTTAAC', 'GATGTCTGTC', 'ACGGCGTTAG', 'CCCTAACGAG', 'CGTCAGAGGT']

print(RandomMotifs(Dna, k,t))
