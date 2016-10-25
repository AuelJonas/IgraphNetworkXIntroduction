
# coding: utf-8

# # Igraph introduction

# In[1]:

import igraph as ig
import numpy as np

g = ig.Graph()

g.add_vertices(3)
ig.plot(g, bbox = (100, 100))


# In[2]:

g.add_edges([(0,1), (1,2)])
ig.plot(g, bbox = (100, 100))


# In[3]:

g.delete_vertices(2)
ig.plot(g, bbox = (100, 100))


# In[4]:

g = ig.Graph(directed = True)
g.add_vertices(3)
g.add_edges([(0, 1), (1, 2)])
ig.plot(g, bbox = (100, 100))


# In[5]:

g = ig.Graph.Tree(10,3)
ig.plot(g, bbox = (300,300))


# In[6]:

g = ig.Graph.Full(4)
ig.plot(g, bbox = (300,300))


# In[7]:

g = ig.Graph( [(0,1), (0,2), (0,3),(1,2),(1,4),(2,5),(2,4),(3,5),(4,6),(5,6)])
g.vs["name"] = ["MA", "HD", "SP", "KA", "S", "F", "M"]
g.vs["label"] = g.vs["name"]
ig.plot(g,layout = g.layout("sugiyama"), bbox = (600,300))


# In[8]:

g.is_weighted()


# In[9]:

g.es["weight"] = 1.0
g.es["weight"] = [5, 6, 6, 4, 7, 5, 4, 5, 7]
ig.plot(g,layout = g.layout("sugiyama"), bbox = (600,300), edge_width = g.es["weight"])


# # Example on a social network

# In[17]:

g = ig.Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
names = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["name"] = names
g.vs["label"] = g.vs["name"]
ig.plot(g, layout = g.layout("sugiyama"), bbox = (600, 300),inline = False)


# In[11]:

print g


# In[12]:

g.degree()


# In[13]:

import pandas as pd

hubscore = g.hub_score()
beetweeness = g.betweenness()
d = {"hub score": hubscore, "beetweeness": beetweeness}
pd.DataFrame(d, index = names)


# In[14]:

A = np.matrix(g.get_adjacency().data)
AtA = A.transpose() * A
w, v = np.linalg.eig(AtA)
maxeigen =  np.argmax(w)
maxv =  max(v[:,maxeigen])
hubs = np.multiply((1/maxv), v[:,maxeigen])
hubs = hubs.A1

d = {"hub score": hubs}
pd.DataFrame(d, index = names)


# In[ ]:



