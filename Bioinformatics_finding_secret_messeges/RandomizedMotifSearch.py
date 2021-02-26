## for this assignment I rewritte some functions to work better

import random
import os
repo=os.getcwd()
def Pr(Text, Profile):
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p


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

def ProfileMostProbableKmer(text, k , profile):
    most_probal=0
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        prob_kmer=Pr(kmer,profile)
        if prob_kmer>most_probal:
            most_probal=prob_kmer
            most_probkmer=kmer
    return most_probkmer

def Motifs(profile,Dna,k):
    Motif=[]
    for dnastring in Dna:
        Motif.append(ProfileMostProbableKmer(dnastring,k,profile))
    return Motif

def RandomizedMotifSearch(Dna, k, t):
    M=RandomMotifs(Dna,k,t)
    BestMotifs=M[:]

    while True:
        current_profile = ProfileWithPseudocounts(M)
        M = Motifs(current_profile, Dna,k)
        score=Score(M)
        BestScore=Score(BestMotifs)
        if score < BestScore:
            BestScore=score
            BestMotifs=M[:]
        else:
            return BestMotifs 

def iterations_RandomMotifSearch(Dna,k,t):
    bmotif=RandomizedMotifSearch(Dna,k,t)
    for i in range(1000):
        RndmMotif=RandomizedMotifSearch(Dna,k,t)
        if Score(bmotif)>Score(RndmMotif):
            bmotif=RndmMotif[:]
        else:
            bmotif=bmotif[:]
    return bmotif

with open(repo+"/texts/randsearch.txt","r") as reader:
    data=reader.readlines()
for i in range(len(data)):
    data[i]=data[i].strip()

k=int((data[0].split(" "))[0])
t=int((data[0].split(" "))[1])
Dna=data[1:]
random.seed(0)

#print(*iterations_RandomMotifSearch(Dna,k,t),sep="\n")

Dna=["AAGCCAAA",
"AATCCTGG",
"GCTACTTG",
"ATGTTTTG"]
Rmot=["CCA","CCT","CTT","TTG"]
x=Motifs(ProfileWithPseudocounts(Rmot),Dna,3)
print(x)
