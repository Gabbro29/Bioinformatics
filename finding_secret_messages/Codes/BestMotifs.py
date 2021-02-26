def Count(Motifs):
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
                count['A'].append(counter_A)
            elif sym=='C':
                count['C'].append(counter_C)
            elif sym=='G':
                count['G'].append(counter_G)
            elif sym=='T':
                count['T'].append(counter_T)
    return count


def Profile(motifs):
    count2=Count(motifs)

    for sym in 'ACGT':
        for col in range(len(count2[sym])):
            count2[sym][col]=count2[sym][col]/len(motifs)
    
    return count2

def Consensus(motfis):

    pro2=Profile(motfis)
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

def ProfileMostProbableKmer(text, k , profile):
    pro_max=-1
    k_mer_max=''
    for i in range(len(text)):
        k_mer=text[i:i+k]
        if len(k_mer)==k:
            if Pr(k_mer, profile)>pro_max :
                pro_max=Pr(k_mer,profile)
                k_mer_max=k_mer
    return k_mer_max

def GreedyMotifSearch(Dna, k, t):
    BestMotifs=[]
    for i in range(t):
        BestMotifs.append(Dna[i][0:k])

    #print(BestMotifs)
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

Dna = ["GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"
]
#print(Dna)

print(GreedyMotifSearch(Dna, 3, 5))
