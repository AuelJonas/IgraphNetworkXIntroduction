#!/usr/bin/env python

import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
import random 

"create Graph using NetworkX:"
G = nx.Graph()
i = 0
for i in range(0, 10):
    G.add_edge(random.randrange(0,10,1), random.randrange(0,10,1))
"is G connected?"
print(nx.is_connected(G))
"plot"
nx.draw_networkx(G)
plt.title("Randomly created graph (10 edges)")
plt.show()
	

"visualize example data graph:"
H = nx.read_gml("/home/sven/Downloads/dolphins.gml", relabel = True)
print(nx.is_connected(H))
nx.draw_networkx(H)
plt.title("Graph representation of interaction between dolphins")
plt.show()

"""try igraph for same visualization:"
G = ig.load("/home/sven/Downloads/dolphins.gml")
ig.plot(G)
"""

"""
# Graph example
# create empty Graph
G = nx.Graph()
# add node(s)
G.add_nodes_from([3,4,5,6])
# add edge(s)
G.add_edges_from([(4,5), (3,6), (4,6)])

# inspect Graph
#print(G.number_of_nodes())
#print(G.number_of_edges())
print("neighbors of 6:")
print(G.neighbors(6))
print("degree of G:")
print(nx.degree(G))
"""
