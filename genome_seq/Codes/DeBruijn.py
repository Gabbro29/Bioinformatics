import os
repo=os.getcwd()
from collections import defaultdict

def Preffix(pattern):
    return pattern[0:len(pattern)-1]
def Suffix(pattern):
    return pattern[1:len(pattern)]

def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

def DeBruijn(k,dna_string):
    dic_rel=defaultdict(list)
    for i in range(len(dna_string)-k+2):
        key=dna_string[i:i+k-1]
        if i+k<=len(dna_string):
            dic_rel[key].append(dna_string[i+1:i+k])
    relations=[]
    for key in dic_rel:
        ed=[]
        ed.append(key)
        goto=[]
        for edges in dic_rel[key]:
            goto.append(edges)
        eds=",".join(goto)
        ed.append(eds)
        gra=" -> ".join(ed)
        relations.append(gra)

    return relations

with open(repo+"/genome_seq/inputs/debru.txt","r") as reader:
    debru=list(map(str.strip,reader.readlines()))
    k=int(debru[0])
    dna_str=debru[1]
    relat=DeBruijn(k,dna_str)
    out_relat="\n".join(relat)
with open(repo+"/genome_seq/outputs/debru_solve.txt","w") as writter:
    writter.write(out_relat)

