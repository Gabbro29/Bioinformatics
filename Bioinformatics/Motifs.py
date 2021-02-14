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


def Motifs(Profile, Dna):
    motifs=[]
    t=len(Dna)
    k=3 #K-MER QUE PIDEN
    for i in range(t):
        motif=ProfileMostProbableKmer(Dna[i],k,Profile) # analizo dna por dna cual es el mas probalbel
        motifs.append(motif)
    return motifs

