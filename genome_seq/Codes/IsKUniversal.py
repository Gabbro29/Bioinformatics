def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

def IsKUniversal(k,str):
    comp=Composition(k,str)
    for elem in comp:
        if comp.count(elem)!=1:
            return False
    return True

print(IsKUniversal(3,"0111010001"))