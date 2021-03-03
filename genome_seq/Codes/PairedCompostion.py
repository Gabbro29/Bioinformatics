def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

def PairedComposition(k,d,string):
    pairs=[]
    comp=Composition(k,string)
    for i in range(len(comp)-(k+d)):
        par=[comp[i],comp[i+k+d]]
        pairs.append(par)
    return pairs

