from collections import defaultdict
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
        par=comp[i]+"|"+comp[i+k+d]
        pairs.append(par)
    return pairs


def PrefixPair(pair):
    pares=pair.split("|")
    return [pares[0][0:len(pares[0])-1],pares[1][0:len(pares[1])-1]]

def SuffixPair(pair):
    pares=pair.split("|")
    return [pares[0][1:],pares[1][1:]]

def PairedDebruijnGraph(k,d,Text):
    pares=PairedComposition(k,d,Text)
    conection_dic={}
    for par in pares:
        conection_dic[par]=[]
        for par2 in pares:
            if par!=par2 and SuffixPair(par)==PrefixPair(par2):
                conection_dic[par].append(par2)
    return conection_dic

print(PairedDebruijnGraph(3,1,"TAATGCCATGGGATGTT"))