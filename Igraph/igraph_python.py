# # Igraph introduction

# importing packages
import igraph as ig
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# initilize an undirected empty graph
g = ig.Graph()

# adding 3 vertices
g.add_vertices(3)
ig.plot(g, bbox = (100, 100))

# add an edge from 0 to 1 and from 1 to 2
g.add_edges([(0,1), (1,2)])
ig.plot(g, bbox = (100, 100))

# delete the 2nd vertex
g.delete_vertices(2)
ig.plot(g, bbox = (100, 100))

# initializing a directed graph
g = ig.Graph(directed = True)

# add vertices and edges
g.add_vertices(3)
g.add_edges([(0, 1), (1, 2)])
ig.plot(g, bbox = (300, 100))

# creating tree
g = ig.Graph.Tree(6,3)
ig.plot(g, bbox = (300,300))

# creating full graph
g = ig.Graph.Full(4)
ig.plot(g, bbox = (200,200))

g = ig.Graph( [(0,1), (0,2), (0,3),(1,2),(1,4),(2,5),(2,4),(3,5),(4,6),(5,6)])
print g

# name vertices
g.vs["name"] = ["MA", "HD", "SP", "KA", "S", "F", "M"]
# name the labels of the vertices
g.vs["label"] = g.vs["name"]
print g
# plot graph
ig.plot(g,layout = g.layout("sugiyama"), inline = False)

ig.summary(g)

# set edge weight true
g.es["weight"] = 1.0
# add weights to graph
g.es["weight"] = [5, 6, 6, 4, 7, 5, 4, 5, 7]
ig.plot(g,layout = g.layout("sugiyama"), edge_width = g.es["weight"], inline = False)

ig.summary(g)


# # Example of hub and auth. score on a citation network

##
# L. A. Adamic and N. Glance, 
# "The political blogosphere and the 2004 US Election", 
# in Proceedings of the WWW-2005 Workshop on the Weblogging Ecosystem (2005)
##

# importing the Data Set
g = ig.Graph.Read_GML("polblogs.gml")
ig.summary(g)

# calculating the hub score and selecting the top n pages
n = 10
hubscore = np.asarray(g.hub_score())
hubtop = np.argsort(hubscore)[::-1]
d = {"hub score top":hubscore[hubtop[:n]]}
labels = np.asarray(g.vs["label"])
pd.DataFrame(d, index=labels[hubtop[:n]])

# calculating the hub score step by step
A = np.matrix(g.get_adjacency().data)
AAt =  A * A.transpose()
w, v = np.linalg.eig(AAt)
maxeigen =  np.argmax(w)
maxv =  max(v[:,maxeigen])
hubscore = np.multiply((1/maxv), v[:,maxeigen])
hubscore = hubscore.A1

hubtop = np.argsort(hubscore)[::-1]
d = {"hub score top": hubscore[hubtop[:n]]}
labels = np.asarray(g.vs["label"])
pd.DataFrame(d, index=labels[hubtop[:n]])

# calculating the auth. score and slecting the top n pages
authscore = np.asarray(g.authority_score())
authtop = np.argsort(authscore)[::-1]
d = {"auth. score top": authscore[authtop[:n]]}
pd.DataFrame(d, index=labels[authtop[:n]])

# top 10 auth. and hub scores
d = {"auth. top": labels[authtop[:n]], "hub top": labels[hubtop[:n]]}
pd.DataFrame(d)

# calculating how many blogs are in the top k hub and auth.
k = [10, 20, 40, 80, 160, 320, 640, 1280]
same = np.zeros(np.size(k))
counter = 0
for n in k:
    same[counter] = 0
    for i in range(0,n):
        for j in range(0,n):
            if labels[authtop[i]] == labels[hubtop[j]]:
                same[counter] += 1
    counter += 1
plt.plot(k,same/k * 100,'blue')
plt.plot(k,same/k * 100,'ro')
plt.show()

