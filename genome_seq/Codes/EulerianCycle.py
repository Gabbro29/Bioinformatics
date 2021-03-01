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
    dic_nodes=dict.fromkeys(nodes:[] for nodes in dic_graph)
    return dic_nodes


def EulerianGraphs(Graph,mode="Cycle"):
    relations=AdjListToDict(Graph) ## representations of the adj list of the graph
    nodes=[i for i in relations]
    ## this is the first node that we visit
    if mode = "cycle":
        curr_node=str(random.choices(nodes)[0])
    if mode="path":

    curr_path=[curr_node]
    circuit=[]
    
    while curr_path:
        curr_node=curr_path[-1]
        ## if there are more nodes to visit
        if relations[curr_node]:
            ## we eliminate and save the last node that we can visit
            next_node=relations[curr_node].pop()
            curr_path.append(next_node)
        else:
            circuit.append(curr_path.pop())


    return "->".join(circuit[::-1])

##graph=["0 -> 3","1 -> 0","2 -> 1,6","3 -> 2","4 -> 2","5 -> 4","6 -> 5,8","7 -> 9","8 -> 7","9 -> 6"]
##print(EulerianCycle(graph))

with open(repo+"/genome_seq/inputs/eulercycle.txt","r") as reader:
    graph_input=list(map(str.strip,reader.readlines()))
    graph_output=EulerianCycle(graph_input, mode="cycle")
with open(repo+"/genome_seq/outputs/eulercycle_solve.txt","w") as writter:
    writter.write(graph_output)