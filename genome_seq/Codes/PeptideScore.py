import CyclicSpectrum as cs
import LinearSpectrum as ls
import os
def PeptideScore(aminoacid,spectrum,mode="cyclo"):
    if mode=="cyclo":
        amino_cs=cs.CyclicSpectrum(aminoacid)
    if mode=="linear":
        amino_cs=ls.LinearSpectrum(aminoacid)
    score=0
    for aa in set(spectrum):
        score+=min(amino_cs.count(aa),spectrum.count(aa))
    return score


if __name__=="__main__":
    repo=os.getcwd()

    with open(repo+"/genome_seq/inputs/cycloscore.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        score=PeptideScore(inp[0],list(map(int,inp[1].split(" "))))
    with open(repo+"/genome_seq/outputs/cycloscore_solve.txt","w") as writter:
        writter.write(str(score))