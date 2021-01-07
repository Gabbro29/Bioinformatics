import random


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

def Normalize(Probabilities):
    P=Probabilities
    normal={}
    #print(P.items())
    for k,v in Probabilities.items():
        #print(k,v) #k=valor de la biblioteca y v= valor que contiene los valores de la libreria
        #print(P.values)
        normal[k]=P[k]/sum(P.values())
    return normal
prob={'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}

def WeightedDie(Probabilities):
    P=Probabilities
    n=random.uniform(0,1)
    #print(Probabilities.items())
    for p,v in Probabilities.items():
        n-=v
        if n<=0:
            return(p)

def Pr(Text, Profile):
    pro=1
    for col in range(len(Profile['A'])):
        if Text[col]=='A':
            pro=pro*Profile['A'][col]
        elif Text[col]=='C':
            pro=pro*Profile['C'][col]
        elif Text[col]=='G':
            pro=pro*Profile['G'][col]
        elif Text[col]=='T':
            pro=pro*Profile['T'][col]
    return pro

def ProfileGeneratedString(Text, profile, k):
    n=len(Text)
    probabilities={}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]]=Pr(Text[i:i+k],profile)
    probabilities=Normalize(probabilities)
    return WeightedDie(probabilities)

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

def GibbsSampler(Dna, k, t, N):
    motifs=RandomMotifs(Dna, k , t)
    #print(motifs)
    bestmotifs=motifs
    for j in range(1,N):
        i=random.randint(0,t-1)
        motifs.pop(i)
        profile=ProfileWithPseudocounts(motifs)
        motif_i_new=ProfileGeneratedString(Dna[i],profile,k)
        motifs.insert(i,motif_i_new)
        if Score(motifs)<Score(bestmotifs):
            bestmotifs=motifs
    return bestmotifs


print(GibbsSampler(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA'],8,5,100))