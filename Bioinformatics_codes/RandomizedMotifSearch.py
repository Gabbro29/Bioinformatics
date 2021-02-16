
#import the random package here

import random
 
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):

    M=RandomMotifs(Dna, k ,t)
    BestMotifs=M

    while True:
        #print(M)
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)

        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 


# Insert necessary subroutines here, including  esta RandomMotifs(), esta ProfileWithPseudocounts(), esta Motifs(), Score(),
# and any subroutines that these functions need.
def Pr(Text, Profile):

    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]

    return p


def Motifs(pf,dna):

    k = len(pf['A'])
    D = []
    for i in range(0,len(dna)):
        km = []
        sc = []
        for kk in range(len(dna[i])-k+1):
            km += [dna[i][kk:kk+k]]
        for i in km:
            sc += [Pr(i,pf)]
        D += [km[sc.index(max(sc))]]
    return D


def RandomMotifs(Dna, k, t):
    

    cant_nucl=len(Dna[0])
    random_motifs=[]
    for j in range(t):
        ran_po=random.randint(0,cant_nucl-k)
        random_motifs.append(Dna[j][ran_po:k+ran_po])
    return random_motifs

def CountWithPseudocounts(Motifs):
    mot=Motifs
    count={'A':[],'C':[],'G':[],'T':[]}
    
    for col in range(len(mot[0])):
        counter_A=1
        counter_C=1
        counter_G=1
        counter_T=1
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
                count['A'].append(counter_A)
            elif sym=='C':
                count['C'].append(counter_C)
            elif sym=='G':
                count['G'].append(counter_G)
            elif sym=='T':
                count['T'].append(counter_T)
    return count

def ProfileWithPseudocounts(Motifs):
    mot=Motifs
    count2=CountWithPseudocounts(mot)
    count3=CountWithPseudocounts(mot)
    for sym in 'ACGT':
        for col in range(len(count2[sym])):
            cant_nu=count3['A'][col]+count3['C'][col]+count3['G'][col]+count3['T'][col]
            #print(cant_nu)
            count2[sym][col]=float(count2[sym][col]/cant_nu)
    
    return count2



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

print(RandomizedMotifSearch(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA'],8,5))

