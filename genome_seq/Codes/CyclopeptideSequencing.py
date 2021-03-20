from collections import defaultdict
from os import getcwd
repo=getcwd()

def GenerateMassTable():
    with open(repo+"/genome_seq/codes/integer_mass_table.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        pairs=list(map(str.split,inp))
        pairs=list(map(tuple,pairs))
    pairs_dic={pair[0]:int(pair[1]) for pair in pairs}
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
    expanding_yes=[]
    for elem in expanding:
        if Consistency(elem,spectrum,mode="linear")==True:
            expanding_yes.append(elem)
    return expanding_yes
    

def LinearSpectrum(Peptide,alphabet=GenerateAminoAc(),AminoAcidMass=GenerateMassTable()):
    PrefixMass=defaultdict(int)
    PrefixMass[0]=0
    for pep,count in zip(Peptide,range(1,len(Peptide)+1)):
        PrefixMass[count]=PrefixMass[count-1]+AminoAcidMass[pep]
    linear_spectrum=[0]
    for x in range(len(Peptide)):
        for y in range(x+1,len(Peptide)+1):
            linear_spectrum.append(PrefixMass[y]-PrefixMass[x])
    return sorted(linear_spectrum)

def Consistency(peptide,spectrum,mode="linear"):
    if mode=="linear":
        peptide_spectrum=LinearSpectrum(peptide)
        for spect in peptide_spectrum:
            if spect not in spectrum:
                return False
        if Mass(peptide)>ParentMass(spectrum):
            return False
        return True
        
    elif mode=="cyclo":
        peptide_cyclospectrum=CyclicSpectrum(peptide)
        for spect in peptide_cyclospectrum:
            if spect not in spectrum:
                return False
        if Mass(peptide)>ParentMass(spectrum):
            return False
        return True
        
def FromPeptideToMass(peptide):
    mass_peptide=[]
    tableofmasses=GenerateMassTable()
    for aa in peptide:
        mass_peptide.append(str(tableofmasses[aa]))
    return "-".join(mass_peptide)

def CyclopeptideSequencing(Spectrum):
    CandidatePeptides=[]
    FinalPeptides=[]
    CandidatePeptides=Expand(CandidatePeptides,Spectrum)
    veces=0
    while CandidatePeptides:
        veces+=1
        for Peptide in CandidatePeptides:
            if Mass(Peptide)==ParentMass(Spectrum):
                if (CyclicSpectrum(Peptide)==Spectrum) and (Peptide not in FinalPeptides):
                    FinalPeptides.append(Peptide)
        CandidatePeptides=Expand(CandidatePeptides,Spectrum)
    FinalFinalPeptides=[]
    for pep in FinalPeptides:
        if (Consistency(pep,Spectrum,mode="cyclo")==True):
            FinalFinalPeptides.append(pep)
    return FinalFinalPeptides

def EliminateRepitedMasses(peptide_list):
    peptide_as_masses=list(map(FromPeptideToMass,peptide_list))
    no_repited=[]
    for pep in peptide_as_masses:
        if pep not in no_repited:
            no_repited.append(pep)
    return no_repited

if __name__ == "__main__":      
                
    with open(repo+"/genome_seq/inputs/cyclopeptidesequencing.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        spectrum=list(map(int,inp[0].split(" ")))
        sequencing=EliminateRepitedMasses(CyclopeptideSequencing(spectrum))
        out=" ".join(sequencing)
    with open(repo+"/genome_seq/outputs/cyclopeptidesequencing_solve.txt","w") as writter:
        writter.write(out)
