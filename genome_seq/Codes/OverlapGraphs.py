import os 

repo=os.getcwd()

def Preffix(pattern):
    return pattern[0:len(pattern)-1]
def Suffix(pattern):
    return pattern[1:len(pattern)]

def OverlapGraphs(patterns):
    graph=[]
    for elem in patterns:
        relation=[elem]
        nto=[]
        for elem2 in patterns:
            if elem != elem2 and Suffix(elem)==Preffix(elem2):
                nto.append(elem2)
        conections=",".join(nto)
        relation.append(conections)
        if len(nto)!=0:
            graph.append(" -> ".join(relation))
        
    return graph
#patterns=["ATGCG",
#"GCATG",
#"CATGC",
#"AGGCA",
#"GGCAT",
#"GGCAC"]

#print(OverlapGraphs(patterns))

with open(repo+"/genome_seq/inputs/overlapgraphs.txt","r") as reader:
    overlapgraphs=list(map(str.strip,reader.readlines()))
    patterns=overlapgraphs[:]
    graph=OverlapGraphs(patterns)
    graph_out="\n".join(graph)
with open(repo+"/genome_seq/outputs/overlapgraphs_solve.txt","w") as writter:
    writter.write(graph_out)