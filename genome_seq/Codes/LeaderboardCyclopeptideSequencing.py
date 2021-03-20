from os import getcwd
import CyclopeptideSequencing as cseq
import PeptideScore as ps
repo=getcwd()

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    leaderboard=[]
    leaderPeptide=""
    leaderboard=cseq.Expand(leaderboard,Spectrum)
    while leaderboard:
        for peptide in leaderboard:
            if cseq.Mass(peptide)==cseq.ParentMass(Spectrum):
                if ps.PeptideScore(peptide,Spectrum)>ps.PeptideScore(leaderPeptide,Spectrum):
                    leaderboard=peptide
        leaderboard=Trim(leaderboard,Spectrum,N)
        cseq.Expand(leaderboard,Spectrum)
    return leaderPeptide

print()