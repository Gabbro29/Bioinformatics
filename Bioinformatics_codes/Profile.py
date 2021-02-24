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
motfis=["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]

print(CountWithPseudocounts(motfis))

print(Count(motfis))
print(Profile(motfis))
print(ProfileWithPseudocounts(motfis))