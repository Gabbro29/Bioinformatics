import os 
from collections import defaultdict
repo=os.getcwd()

def Preffix(pattern):
    return pattern[0:len(pattern)-1]
def Suffix(pattern):
    return pattern[1:len(pattern)]

def CompositionGraph(patterns):
    # format: dictionary where the key is the edge and the elements of it are a list, where the first element 
    #         is the starting node and the second element is the ending node
    dic_com=defaultdict(list)
    for kmer in patterns:
        nodes=[Preffix(kmer),Suffix(kmer)]
        dic_com[kmer].append(nodes)
    return dic_com

def DeBruijn_kmers(patterns):
    conections=defaultdict(list)
    comgraph=CompositionGraph(patterns)
    for key in comgraph:
        for nodes in comgraph[key]:
            conections[nodes[0]].append(nodes[1])
    graph=[]
    for key1 in conections:
        in_node=str(key1)
        end_node=",".join(conections[key1])
        graph.append(" -> ".join([in_node,end_node]))
    return graph

with open(repo+"/genome_seq/inputs/debru_kmer.txt","r") as reader:
    debru_kmer=list(map(str.strip,reader.readlines()))
    graph="\n".join(DeBruijn_kmers(debru_kmer))    
with open(repo+"/genome_seq/outputs/debru_kmersolve.txt","w") as writter:
    writter.write(graph)

