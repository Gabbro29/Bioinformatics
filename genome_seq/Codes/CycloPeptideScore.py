import CyclicSpectrum as cs
import os
def CycloPeptideScore(aminoacid,spectrum):
    amino_cs=cs.CyclicSpectrum(aminoacid)
    spec=list(map(int,spectrum.split(" ")))
    score=0
    for aa in set(spec):
        score+=min(amino_cs.count(aa),spec.count(aa))
    return score



if __name__=="__main__":
    repo=os.getcwd()

    with open(repo+"/genome_seq/inputs/cycloscore.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        score=CycloPeptideScore(inp[0],inp[1])

    with open(repo+"/genome_seq/outputs/cycloscore_solve.txt","w") as writter:
        writter.write(str(score))