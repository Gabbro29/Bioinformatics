def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

def PrefixPair(pair):
    pares=pair.split("|")
    return [pares[0][0:len(pares[0])-1],pares[1][0:len(pares[1])-1]]

def SuffixPair(pair):
    pares=pair.split("|")
    return [pares[0][1:],pares[1][1:]]

def PairedComposition(k,d,string):
    pairs=[]
    comp=Composition(k,string)
    for i in range(len(comp)-(k+d)):
        par=comp[i]+"|"+comp[i+k+d]
        pairs.append(par)
    return pairs

def PathGraph(k,d,dna_string):
    pares=PairedComposition(k,d,dna_string)
    nodes=[PrefixPair(pares[0])]
    for par in pares:
        nodes.append(SuffixPair(par))
    return nodes

print(PathGraph(3,1,"TAATGCCATGGGATGTT"))