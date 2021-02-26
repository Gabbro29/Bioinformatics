import random
import os
repo=os.getcwd()
### this problem was solved using the RandomizedMotifSearch algorithm
def RandomMotifs(Dna, k, t):
    cant_nucl=len(Dna[0])
    random_motifs=[]
    for dna_string in Dna:
        ran_po=random.randint(0,cant_nucl-k)
        random_motifs.append(dna_string[ran_po:k+ran_po])
    return random_motifs

def CountWithPseudocounts(Motifs):
    mot=Motifs
    count={'A':[],'C':[],'G':[],'T':[]}
    for col in range(len(mot[0])):
        counter_A=0
        counter_C=0
        counter_G=0
        counter_T=0
        for fil in range(len(mot)):
            if mot[fil][col]=='A':
                counter_A+=1
            elif mot[fil][col]=='C':
                counter_C+=1
            elif mot[fil][col]=='G':
                counter_G+=1
            elif mot[fil][col]=='T':
                counter_T+=1
        for sym in 'ACGT':
            if sym=='A':
                count['A'].append(counter_A+1)
            elif sym=='C':
                count['C'].append(counter_C+1)
            elif sym=='G':
                count['G'].append(counter_G+1)
            elif sym=='T':
                count['T'].append(counter_T+1)
    return count

def ProfileWithPseudocounts(Motifs):
    profile={'A':[],'C':[],'G':[],'T':[]}
    pseudocount=CountWithPseudocounts(Motifs)
    for x in pseudocount:
        for y in pseudocount[x]:
            prob=y/int(len(Motifs)+4)
            profile[x].append(prob)
    return profile

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p *= Profile[Text[i]][i]
    return p

def ProfileGeneratedString(Text, profile, k):
    strings=[]
    probabilities=[]
    for i in range(len(Text)-k+1):
        strings.append(Text[i:i+k])
        probabilities.append(Pr(Text[i:i+k],profile))
    selected_motif=random.choices(population=strings,weights=probabilities,k=1)[0]
    return selected_motif

def Consensus(motfis):
    pro2=ProfileWithPseudocounts(motfis)
    code=""
    for col in range(len(motfis[0])):
        symi="A"
        for sym in ("ACGT"):
            if pro2[sym][col]>pro2[symi][col]:
                symi=sym
        code+=symi
    return code

def Score(motfis):
    score=0
    consen=Consensus(motfis)
    for col in range(len(motfis[0])):
        dif=0
        for fil in range(len(motfis)):
            if consen[col]!=motfis[fil][col]:
                dif+=1
        score+=dif
    return score

def GibbsSampler(Dna, k ,t, N,repeticiones=20):
    random.seed(0)
    inicio=True
    for iteration in range(repeticiones):
        if inicio:
            motifs=RandomMotifs(Dna,k,t)
            BestMotifs=motifs[:]
            inicio=False
        for j in range(N):
            index=random.randint(0,t-1)
            motifs.pop(index)
            profile_i=ProfileWithPseudocounts(motifs)
            mot_i=ProfileGeneratedString(Dna[index],profile_i,k)
            motifs.insert(index,mot_i)
            i_motifs_score=Score(motifs)
            Bmotifs_score=Score(BestMotifs)
            if i_motifs_score<Bmotifs_score:
                BestMotifs=motifs[:]
                Bmotifs_score=i_motifs_score
    return BestMotifs


with open(repo+"/texts/gibbs.txt",'r') as reader:
    gibbs=reader.read().splitlines()
    params=gibbs.pop(0).split(" ")
    k=int(params[0])
    t=int(params[1])
    N=int(params[2])
    Dna=gibbs
#print(k,t,N,Dna)
    
Dna=["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA",
"GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
"TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
"TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
"AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
k=8
t=5
N=100
print(*GibbsSampler(Dna,k,t,N,repeticiones=20),sep="\n")