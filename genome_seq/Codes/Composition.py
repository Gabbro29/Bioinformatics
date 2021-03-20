import os
repo=os.getcwd()
def Composition(k,dna_string):
    comp=[]
    for i in range(len(dna_string)-k+1):
        kmer=dna_string[i:i+k]
        comp.append(kmer)
    return comp

with open(repo+"/genome_seq/inputs/composition.txt","r") as reader:
    comp=list(map(str.strip,reader.readlines()))
    dna_string=comp[1]
    k=int(comp[0])
composition=Composition(k,dna_string)
comp_out="\n".join(composition)
with open(repo+"/genome_seq/outputs/composition_solv.txt","w") as writter:
    writter.write(comp_out)