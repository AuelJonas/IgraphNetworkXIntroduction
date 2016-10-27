#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd

# Undirected Graph:
G = nx.Graph()
# create nodes:
List_of_nodes = [1, 2, 3, 5, "Jonas", "Sven"]
G.add_nodes_from(List_of_nodes)
nx.draw_networkx(G)
plt.show()
	
# create edges:
List_of_edges = [(1,2), (2,"Jonas"), (1,3), (3,5), (2,3), ("Sven",1), ("Sven",2), ("Sven",3), ("Sven",5)]
G.add_edges_from(List_of_edges)
nx.draw_networkx(G)
plt.show()

# remove nodes:
G.remove_node(2)
nx.draw_networkx(G)
plt.show()

# create random graph:
H = nx.Graph()
# Graph can be created by only adding edges:
for i in range(0, 10):
    H.add_edge(random.randrange(0,10,1), random.randrange(0,10,1))
nx.draw_networkx(H)
plt.show()
print("number of edges in H: %d" % nx.number_of_edges(H))
print(H.nodes())
print(H.edges())

# Directed Graph:
I = nx.DiGraph()
List_of_edges = [("Max","Peter"), ("Peter","Jonas"), ("Max","Till"), ("Till","Luisa"), ("Jonas","Luisa"), 
                 ("Peter","Till"), ("Sara","Max"), ("Sara","Peter"), ("Sara","Till"), ("Sara","Luisa")]
I.add_edges_from(List_of_edges)
nx.draw_networkx(I)
plt.title("distribution of exercise solutions through students")
plt.show()

# MultiDiGraph:
J = nx.MultiDiGraph()
J.add_edges_from(I.edges())
J.add_edge("Sara","Peter")
nx.draw_networkx(J)
plt.title("distribution of exercise solutions through students")
plt.show()
print(J.edges())
print(I.edges())

### ANALYZING NETWORKS USING NETWORKX ###

# create undirected network from I:
I = I.to_undirected()
nx.draw_networkx(I)
plt.title("example social network")
plt.show()
# analyze graph I
print("number of nodes in I: %d" % I.number_of_nodes())
print("number of edges in I: %d" % I.number_of_edges())
print("Sara is friends with:") 
print(I.neighbors("Sara"))
print("degree of nodes in I:")
I.degree()
print("Is I connected? %s" % nx.is_connected(I))
print("Is I directed? %s" % nx.is_directed(I))

# adjacency list of I:
print(I.nodes())
I.adjacency_list()

### NETWORK ALGORITHMS ON EXAMPLE DATA ###

# metrics on example social network:
b = nx.betweenness_centrality(I, k = None, normalized = True, endpoints = False, seed = None)
c = nx.closeness_centrality(I)
d = nx.degree_centrality(I)
d = {"Betweenness": b, "Closeness": c, "Degree": d}
nx.draw_networkx(I)
plt.title("example social network")
plt.show()
pd.DataFrame(d)

###
# example data:
# D. Lusseau, K. Schneider, O. J. Boisseau, P. Haase, E. Slooten, and S. M. Dawson, 
# Behavioral Ecology and Sociobiology 54, 396-405 (2003)
###
K = nx.read_gml("dolphins.gml", relabel = True)
b = nx.betweenness_centrality(K)
c = nx.closeness_centrality(K)
d = nx.degree_centrality(K)
dic = {"Betweenness": b, "Closeness": c, "Degree": d}
data = pd.DataFrame(dic)
betweenness_top = data.sort_index(by = "Betweenness", ascending = False)[0:10].index
closeness_top = data.sort_index(by = "Closeness", ascending = False)[0:10].index
degree_top = data.sort_index(by = "Degree", ascending = False)[0:10].index
dic_top = {"Betweenness top": betweenness_top, "Closeness top": closeness_top, "Degree top": degree_top}

nx.draw_networkx(K)
plt.title("Social network of dolphins")
plt.show()
print(pd.DataFrame(dic_top, index = range(1,11)))
