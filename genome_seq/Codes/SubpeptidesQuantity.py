import os
import math
def SubpeptidesQuantity(lenPeptide):
    quantity=1
    for i in range(lenPeptide+1):
        quantity+=i
        #print(i)
    return quantity

with open(os.getcwd()+"/genome_seq/inputs/subpeptide.txt","r") as reader:
    inp=list(map(str.strip,reader.readlines()))[0]
    quantity=SubpeptidesQuantity(int(inp))
with open(str(os.getcwd())+"/genome_seq/outputs/subpeptide_solve.txt","w") as writter:
    writter.write(str(quantity))