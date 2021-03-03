def Preffix(pattern):
    return pattern[0:len(pattern)-1]
def Suffix(pattern):
    return pattern[1:len(pattern)]

def PreffixPair(pair):
    der_pre=Preffix(pair[0])
    iz_pre=Preffix(pair[1])
    return [der_pre,iz_pre]

def SuffixPair(pair):
    return [Suffix(pair[0]),Suffix(pair[1])]

def OverlapGraphs(patterns):
    graph=[]
    for elem in patterns:
        relation=[elem]
        nto=[]
        for elem2 in patterns:
            if elem != elem2 and Suffix(elem)==Preffix(elem2):
                nto.append(elem2)
        conections=",".join(nto)
        relation.append(conections)
        if len(nto)!=0:
            graph.append(" -> ".join(relation))
        
    return graph

def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

def PairedComposition(k,d,string): ## revisar
    pairs=[]
    comp=Composition(k,string)
    for i in range(len(comp)-(k+d)):
        par=[comp[i],comp[i+k+d]]
        pairs.append(par)
    return pairs



def PathGraph(k,d,dna_string):
    pairs=PairedComposition(k,d,dna_string)
    graph=[]
    for elem in pairs:
        relations=["("+"|".join(elem)+")"]
        nto=[]
        for elem2 in pairs:
            if elem!=elem2 and SuffixPair(elem) == PreffixPair(elem2):
                nto.append(elem2)
                #print(elem2)
        if len(nto)!=0: 
            nto_pair=["("+"|".join(pair)+")" for pair in nto]
            print(nto_pair)
            conections=",".join(nto_pair)
            relations.append(conections)
            print(relations)
            graph.append(" -> ".join(relations))
    return graph



print(PairedComposition(3,1,"TAATGCCATGGGATGTT"))