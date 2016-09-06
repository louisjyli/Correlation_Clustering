__author__ = 'LouisLi'
import networkx as nx
import random

output=open("size-gplus.txt","a")
G=nx.read_edgelist("gplus.txt")

while G.number_of_nodes()!=0:
    select=random.sample(G.nodes(),1)
    size=len(G.neighbors(select[0]))+1
    output.write(str(size)+"\n")
    rm=G.neighbors(select[0])
    G.remove_node(select[0])
    for i in range(len(rm)):
        G.remove_node(rm[i])

output.close()
