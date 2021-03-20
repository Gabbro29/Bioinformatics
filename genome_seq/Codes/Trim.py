from os import getcwd
import CyclopeptideSequencing as cseq
import PeptideScore as ps

def Trimmer(Leaderboard, Spectrum,N,Alphabet=cseq.GenerateAminoAc(),AminoAcidMass=cseq.GenerateMassTable()):
    linearscore=[]
    for i in range(0,len(Leaderboard)):
        peptide=Leaderboard[i]
        linearscore.append(ps.PeptideScore(peptide,Spectrum,mode="linear"))
    order_leaderboard=[x for _,x in sorted(zip(linearscore,Leaderboard),reverse=True)]
    linearscore.sort(reverse=True)
    for j in range(N+1,len(Leaderboard)):
        if linearscore[j]<linearscore[N]:
            return order_leaderboard[0:j-1]
    return order_leaderboard

if __name__=="__main__":
    with open(getcwd()+"/genome_seq/inputs/trim.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        trimmed=Trim(inp[0].split(" "),list(map(int,inp[1].split(" "))),int(inp[2]))
        out="\n".join(trimmed)

    with open(getcwd()+"/genome_seq/outputs/trim_solve.txt","w") as writter:
        writter.write(out)