
import os
from collections import defaultdict
repo=os.getcwd()
import math

def GenerateMassTable():
    with open(repo+"/genome_seq/codes/integer_mass_table.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        pairs=list(map(str.split,inp))
        pairs=list(map(tuple,pairs))
    pairs_dic={pair[0]:int(pair[1]) for pair in pairs}
    return pairs_dic

def GenerateAminoAc():
    aminoac_letters= ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    return aminoac_letters

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

def Mass(peptide):
    mass=0
    table=GenerateMassTable()
    for aa in peptide:
        mass+=table[aa]
    return mass

def ParentMass(spectrum):
    return max(spectrum)

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


def Trimmer(Leaderboard, Spectrum,N,Alphabet=GenerateAminoAc(),AminoAcidMass=GenerateMassTable()):
    linearscore=[]
    for i in range(0,len(Leaderboard)):
        peptide=Leaderboard[i]
        linearscore.append(PeptideScore(peptide,Spectrum,mode="linear"))
    order_leaderboard=[x for _,x in sorted(zip(linearscore,Leaderboard),reverse=True)]
    linearscore.sort(reverse=True)
    for j in range(N+1,len(Leaderboard)):
        if linearscore[j]<linearscore[N]:
            return order_leaderboard[0:j-1]
    return order_leaderboard

def PeptideScore(aminoacid,spectrum,mode="cyclo"):
    if mode=="cyclo":
        amino_cs=CyclicSpectrum(aminoacid)
    if mode=="linear":
        amino_cs=LinearSpectrum(aminoacid)
    score=0
    for aa in set(spectrum):
        score+=min(amino_cs.count(aa),spectrum.count(aa))
    return score

def LeaderboardCyclopeptideSequencing(N,Spectrum):
    Leaderboard=Expand([],Spectrum)
    LeaderPeptide=""
    while len(Leaderboard):
        t=Leaderboard[:]
        for peptide in t:
            if Mass(peptide)==ParentMass(Spectrum):
                if PeptideScore(peptide, Spectrum)>PeptideScore(LeaderPeptide,Spectrum):
                    LeaderPeptide=peptide
        Leaderboard=Expand(Leaderboard,Spectrum)[:]
        if len(Leaderboard)>N:
            Leaderboard=Trimmer(Leaderboard,Spectrum,N)
        N=math.ceil(N/2)
    return FromPeptideToMass(LeaderPeptide)

def FromPeptideToMass(peptide):
    mass_peptide=[]
    tableofmasses=GenerateMassTable()
    for aa in peptide:
        mass_peptide.append(str(tableofmasses[aa]))
    return "-".join(mass_peptide)

if __name__ == "__main__":      
                
    with open(repo+"/genome_seq/inputs/leader.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        #print(list(map(int,inp[1].split(" "))))
        spectrum=list(map(int,inp[1].split(" ")))
        #print(spectrum)
        n=int(inp[0])
        lea=LeaderboardCyclopeptideSequencing(n,spectrum)
        print(lea)
    #with open(repo+"/genome_seq/outputs/cyclopeptidesequencing_solve.txt","w") as writter:
    #    writter.write(out)
