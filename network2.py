import igraph
g = igraph.Graph.Read_Ncol('edgelist_nu.txt', directed=False)
print igraph.summary(g)
layout = g.layout("kk")
igraph.plot(g, layout = layout)