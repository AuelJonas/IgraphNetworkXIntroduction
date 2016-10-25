import igraph as ig

graph = ig.Graph()
layout = graph.layout('kk')

graph.add_vertices(3)
graph.add_edges([(0,1), (1,2)])
#ig.plot(graph, layout = layout)
#print graph

g = ig.Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["label"] = g.vs["name"]
ig.plot(g, layout = g.layout("kk"), bbox = (600, 300))
