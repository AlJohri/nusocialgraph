import igraph
g = igraph.Graph.Read_Ncol('edgelist.txt', directed=False)
layout = g.layout("kk")
igraph.plot(g, layout = layout)