import os
from collections import defaultdict
repo=os.getcwd()

import os
from collections import defaultdict
repo=os.getcwd()
def GenerateMassTable():
    with open(repo+"/genome_seq/codes/integer_mass_table.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        pairs=list(map(str.split,inp))
        pairs=list(map(tuple,pairs))
    pairs_dic={pair[0]:int(pair[1]) for pair in pairs}
    #print("".join([key for key in pairs_dic]))
    return pairs_dic
def GenerateAminoAc():
    aminoac_letters= ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    return aminoac_letters
def CyclicSpectrum(Peptide,alphabet=GenerateAminoAc(),AminoAcidMass=GenerateMassTable()):
    PrefixMass=defaultdict(int)
    PrefixMass[0]=0
    #print(PrefixMass[0])
    for pep,count in zip(Peptide,range(1,len(Peptide)+1)):
        PrefixMass[count]=PrefixMass[count-1]+AminoAcidMass[pep]
    peptide_mass=PrefixMass[len(Peptide)]
    cyclic_spectrum=[0]
    for x in range(len(Peptide)):
        for y in range(x+1,len(Peptide)+1):
            cyclic_spectrum.append(PrefixMass[y]-PrefixMass[x])
            if x>0 and y<len(Peptide):
                cyclic_spectrum.append(peptide_mass-(PrefixMass[y]-PrefixMass[x]))
    return sorted(cyclic_spectrum)


with open(repo+"/genome_seq/inputs/cyclicspectrum.txt","r") as reader:
    inp=list(map(str.strip,reader.readlines()))
    spectrum=" ".join(list(map(str,CyclicSpectrum(inp[0]))))
with open(repo+"/genome_seq/outputs/cyclicspectrum_solve.txt","w") as writter:
    writter.write(spectrum)