
from os import getcwd
import CyclopeptideSequencing as cseq
import PeptideScore as ps
from Trim import Trimmer
repo=getcwd()

def LeaderboardCyclopeptideSequencing(N, Spectrum):
    leaderboard=[]
    leaderPeptide=""
    leaderboard=cseq.Expand(leaderboard,Spectrum)
    while leaderboard:
        for peptide in leaderboard:
            if cseq.Mass(peptide)==cseq.ParentMass(Spectrum):
                if ps.PeptideScore(peptide,Spectrum)>ps.PeptideScore(leaderPeptide,Spectrum):
                    leaderPeptide=peptide
        leaderboard=cseq.Expand(leaderboard,Spectrum)
        leaderboard=Trimmer(leaderboard,Spectrum,N)
        #print(leaderPeptide)
    return cseq.FromPeptideToMass(leaderPeptide)

#print(LeaderboardCyclopeptideSequencing(10,list(map(int,"0 71 113 129 147 200 218 260 313 331 347 389 460".split(" ")))))
if __name__=="__main__":
    with open(repo+"/genome_seq/inputs/leader.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        lea=LeaderboardCyclopeptideSequencing(int(inp[0]),list(map(int,inp[1].split(" "))))
        print(lea)
        
    #with open(repo+"/genome_seq/outputs/leader_solve.txt","w") as writter:
        #writter.write(lea)