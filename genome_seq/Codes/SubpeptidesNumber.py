import os
repo=os.getcwd()
def SubpeptideNumber(peptide_length):
    return peptide_length*(peptide_length-1)  ## I have n elections then n-1 elections so we multiply it 

with open(repo+"/genome_seq/inputs/numberpeptide.txt","r") as reader:
    inp=list(map(str.strip,reader.readlines()))
    pep_length=int(inp[0])
    number_subpeptides=SubpeptideNumber(pep_length)
with open(repo+"/genome_seq/outputs/numberpeptide_solve.txt","w") as writter:
    writter.write(str(number_subpeptides))