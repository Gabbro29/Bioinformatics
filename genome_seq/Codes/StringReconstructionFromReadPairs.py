from collections import defaultdict
import os 
import random
repo=os.getcwd()

def PrefixPair(pair):
    pares=pair.split("|")
    return pares[0][0:len(pares[0])-1]+"|"+pares[1][0:len(pares[1])-1]

def SuffixPair(pair):
    pares=pair.split("|")
    return pares[0][1:]+"|"+pares[1][1:]

def PairedCompositionGraph(kdmers):
    dic_com=defaultdict(list)
    for elem in kdmers:
        nodes=[PrefixPair(elem),SuffixPair(elem)]
        dic_com[elem].append(nodes)
    return dic_com


def PairedDebruijnGraph(k,d,kdmers):
    conections_dic=defaultdict(list)
    comp=PairedCompositionGraph(kdmers)
    for key in comp:
        for nodes in comp[key]:
            conections_dic[nodes[0]].append(nodes[1])
    graph=[]
    for key in conections_dic:
        conect=key+" -> "+",".join(conections_dic[key])
        graph.append(conect)
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

def UnGrapper(kdmers):
    list_kdmers=[pair.split("|") for pair in kdmers]
    return list_kdmers

def StringSpelledByPatterns(patterns):
    string=""
    k=len(patterns[0])
    for elem in patterns:
        if string=="":
            string+=elem
        else:
            string+=elem[k-1]
    return string
def PrefixSuffixConcatenation(k,d,Prefix,Suffix):
    concatenation=Prefix+Suffix[len(Suffix)-(k+d):len(Suffix)]
    return concatenation

def StringSpelledByGrappedGenomePath(k,d,kdmers):
    li_pairs=UnGrapper(kdmers)
    FirstPatterns=[par[0] for par in li_pairs]
    SecondPatterns=[par[1] for par in li_pairs]
    PrefixString=StringSpelledByPatterns(FirstPatterns)
    SuffixString=StringSpelledByPatterns(SecondPatterns)
    for i in range(1+k+d,len(PrefixString)):
        if PrefixString[i] != SuffixString[i-k-d]:
            return ("there is no string spelled by the gapped patterns")
    return PrefixSuffixConcatenation(k,d,PrefixString,SuffixString)

def StringReconstructionFromReadPairs(k,d,kdmers):
    db=PairedDebruijnGraph(k,d,kdmers)
    path=EulerianGraphs(db,mode="path").split("->")
    dna_string=StringSpelledByGrappedGenomePath(k,d,path)
    return dna_string

with open(repo+"/genome_seq/inputs/reconstrunctionpair.txt","r") as reader:
    ins=list(map(str.strip,reader.readlines()))
    k,d=ins[0].split(" ")
    kdmers=ins[1:]
    out=StringReconstructionFromReadPairs(int(k),int(d),kdmers)

with open(repo+"/genome_seq/outputs/reconstructionpair_solve.txt","w") as writter:
    writter.write(out)