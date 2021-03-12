from collections import defaultdict
from os import getcwd
repo=getcwd()

def GenerateMassTable():
    with open(repo+"/genome_seq/codes/integer_mass_table.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        pairs=list(map(str.split,inp))
        pairs=list(map(tuple,pairs))
    pairs_dic={pair[0]:int(pair[1]) for pair in pairs}
    #print("".join([key for key in pairs_dic]))
    return pairs_dic

def Mass(peptide):
    mass=0
    table=GenerateMassTable()
    for aa in peptide:
        mass+=table[aa]
    return mass

def ParentMass(spectrum):
    return max(spectrum)

def GenerateAminoAc():
    aminoac_letters= ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    return aminoac_letters

def CyclicSpectrum(Peptide,alphabet=GenerateAminoAc(),AminoAcidMass=GenerateMassTable()):
    PrefixMass=defaultdict(int)
    PrefixMass[0]=0
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

def Expand(peptides,spectrum ,amino_acid_mass_table=GenerateMassTable()):
    if peptides==[]:
        expanding=[peptide for peptide in amino_acid_mass_table.keys()]
    else:
        expanding = [peptide + amino_acid for amino_acid in amino_acid_mass_table.keys() for peptide in peptides]
    for elem in expanding:
        if Consistency(elem,spectrum)==False:
            expanding.remove(elem)
    return expanding
    

def LinearSpectrum(Peptide,alphabet=GenerateAminoAc(),AminoAcidMass=GenerateMassTable()):
    PrefixMass=defaultdict(int)
    PrefixMass[0]=0
    #print(PrefixMass[0])
    for pep,count in zip(Peptide,range(1,len(Peptide)+1)):
        PrefixMass[count]=PrefixMass[count-1]+AminoAcidMass[pep]
    linear_spectrum=[0]
    #print(PrefixMass)
    for x in range(len(Peptide)):
        for y in range(x+1,len(Peptide)+1):
            linear_spectrum.append(PrefixMass[y]-PrefixMass[x])
    return sorted(linear_spectrum)

def Consistency(peptide,spectrum):
    peptide_spectrum=LinearSpectrum(peptide)
    for spect in peptide_spectrum:
        if spect in spectrum:   
            quantity_in_spectrum=spectrum.count(spect) ##quantity of times that the mass appears in Spectrum
            quantity_in_peptide_spectrum=peptide_spectrum.count(spect)
            if quantity_in_spectrum != quantity_in_peptide_spectrum:
                return False
        else:
             return False
    if Mass(peptide)>ParentMass(spectrum):
        return False
    return True
        

def CyclopeptideSequencing(Spectrum):
    CandidatePeptides=[]
    FinalPeptides=[]
    CandidatePeptides=Expand(CandidatePeptides,Spectrum)
    while CandidatePeptides:
        for Peptide in CandidatePeptides:
            if Mass(Peptide)==ParentMass(Spectrum):
                if (CyclicSpectrum(Peptide)==Spectrum) and (Peptide not in FinalPeptides):
                    FinalPeptides.append(Peptide)
        CandidatePeptides=Expand(CandidatePeptides,Spectrum)
        print(CandidatePeptides)
    return FinalPeptides

spectrum=list(map(int,["0", "113", "128", "186", "241", "299", "314", "427"]))
print(CyclopeptideSequencing(spectrum))
debugging="a"
#print(Expand([""],spectrum))