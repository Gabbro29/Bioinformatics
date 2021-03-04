from collections import defaultdict

def PrefixPair(pair):
    pares=pair.split("|")
    return pares[0][0:len(pares[0])-1]+"|"+pares[1][0:len(pares[1])-1]

def SuffixPair(pair):
    pares=pair.split("|")
    return pares[0][1:]+"|"+pares[1][1:]

def PairedCompositionGraph(kdmers):
    dic_com=defaultdict(list)
    for elem in kdmers:
        nodes=[PrefixPair(elem),SuffixPair(elem)]
        dic_com[elem].append(nodes)
    return dic_com


def PairedDebruijnGraph(k,d,kdmers):
    conections_dic=defaultdict(list)
    comp=PairedCompositionGraph(kdmers)
    for key in comp:
        for nodes in comp[key]:
            conections_dic[nodes[0]].append(nodes[1])
    return conections_dic

print(PairedDebruijnGraph(3,1,["AAT|CCA","ATG|CAT","ATG|GAT","CAT|GGA","CCA|GGG","GCC|TGG","GGA|GTT","GGG|TGT","TAA|GCC","TGC|ATG","TGG|ATG"]))