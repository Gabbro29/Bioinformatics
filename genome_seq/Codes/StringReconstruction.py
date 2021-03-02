import os 
from collections import defaultdict
import random
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

def AdjListToDict(Graph,):
    adj_list=[elem.split(" -> ") for elem in Graph]
    dic_graph={}
    for nodes in adj_list:
        dic_graph[nodes[0]]=nodes[1].split(",")
    return dic_graph
def outgoing_max(dic_graph):
    ##format of the dictionary, left ingoing nodes, right outgoing nodes
    dic_nodes={}
    for node in dic_graph:
        dic_nodes[node]=[0,0]
        for node2 in dic_graph[node]:
            dic_nodes[node2]=[0,0]
    
    ##outgoing nodes
    for node in dic_nodes:
        try:
            dic_nodes[node][1]+=(len(dic_graph[node]))
        except KeyError:
            dic_nodes[node][1]+=0
    for node in dic_nodes:
        try:
            for conections in dic_graph[node]:
                dic_nodes[conections][0]+=1
        except KeyError:
            pass
    for node3 in dic_nodes:
        if dic_nodes[node3][0]<dic_nodes[node3][1]:
            return node3


def EulerianGraphs(Graph,mode="cycle"):
    relations=AdjListToDict(Graph) ## representations of the adj list of the graph
    nodes=[i for i in relations]
    ## this is the first node that we visit
    if mode =="cycle":
        curr_node=str(random.choices(nodes)[0])
    if mode=="path":
        curr_node=outgoing_max(relations)
    curr_path=[curr_node]
    circuit=[]
    
    while curr_path:
        curr_node=curr_path[-1]
        ## if there are more nodes to visit
        try:
            if relations[curr_node]:
                ## we eliminate and save the last node that we can visit
                next_node=relations[curr_node].pop()
                curr_path.append(next_node)
            else:
                circuit.append(curr_path.pop())
        except KeyError:
            eliminated_node=curr_node
            curr_path.remove(curr_node)
            pass
    try:
        circuit.insert(0,eliminated_node)
        return "->".join(circuit[::-1])
    except UnboundLocalError:
        return "->".join(circuit[::-1])

def PathToGenome(path):
    genome=""
    k=len(path[0])
    for elem in path:
        if genome=="":
            genome+=elem
        else:
            genome+=elem[k-1]
    return genome

def StringReconstruction(k,patterns):
    db=DeBruijn_kmers(patterns)
    path=EulerianGraphs(db,mode="path").split("->")
    dna_string=PathToGenome(path)
    return dna_string
    #path=EulerianGraphs(db,mode="path")

#k=4
#kmers=["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]
#print(StringReconstruction(k,kmers))

with open(repo+"/genome_seq/inputs/stringrecon.txt","r") as reader:
    stringreco=list(map(str.strip,reader.readlines()))
    k=int(stringreco[0])
    kmers=stringreco[1:]
    string_out=StringReconstruction(k,kmers)
with open(repo+"/genome_seq/outputs/stringrecon_solve.txt","w") as writter:
    writter.write(string_out)