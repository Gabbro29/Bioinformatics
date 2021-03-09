import os
from collections import defaultdict
repo=os.getcwd()
def GenerateMassTable():
    with open(repo+"/genome_seq/codes/integer_mass_table.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        pairs=list(map(str.split,inp))
        pairs=list(map(tuple,pairs))
    pairs_dic=dict(pairs)
    #print("".join([key for key in pairs_dic]))
    return pairs_dic

def LinearSpectrum(Peptide,alphabet="GASPVTCILNDKQEMHFRYW",AminoAcidMass=GenerateMassTable()):
    PrefixMass=defaultdict(int)
    PrefixMass[0]=0
    #print(PrefixMass[0])
    for i in range(len(Peptide)):
        for j in alphabet:
            if j==Peptide[i]:
                #print(PrefixMass[i-1])
                #print(int(AminoAcidMass[j]))
                PrefixMass[i]=PrefixMass[i-1]+int(AminoAcidMass[j])
    linear_spectrum=[0]
    for x in range(len(Peptide)):
        for y in range(i+1,len(Peptide)+1):
            linear_spectrum.append(PrefixMass[x]-PrefixMass[y])
    return linear_spectrum
print(LinearSpectrum("NQEL"))