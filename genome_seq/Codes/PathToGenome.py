import os
repo=os.getcwd()
def PathToGenome(path):
    genome=""
    k=len(path[0])
    for elem in path:
        if genome=="":
            genome+=elem
        else:
            genome+=elem[k-1]
    return genome

with open(repo+"/genome_seq/inputs/pathgeno.txt","r") as reader:
    pathgeno=list(map(str.strip,reader.readlines()))
    path=pathgeno
ptog=PathToGenome(path)
with open(repo+"/genome_seq/outputs/pathgeno_solve.txt","w") as writter:
    writter.write(ptog)
