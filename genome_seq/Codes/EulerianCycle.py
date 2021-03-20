import random
import os
repo=os.getcwd()
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

##graph=["0 -> 3","1 -> 0","2 -> 1,6","3 -> 2","4 -> 2","5 -> 4","6 -> 5,8","7 -> 9","8 -> 7","9 -> 6"]
##print(EulerianCycle(graph))

with open(repo+"/genome_seq/inputs/eulercycle.txt","r") as reader:
    graph_input=list(map(str.strip,reader.readlines()))
    graph_output=EulerianGraphs(graph_input, mode="cycle")
with open(repo+"/genome_seq/outputs/eulercycle_solve.txt","w") as writter:
    writter.write(graph_output)