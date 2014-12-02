import igraph
g = igraph.Graph.Read_Ncol('edgelist_nu.txt', directed=False)
# Read_Edgelist
print igraph.summary(g)
g.simplify()
print igraph.summary(g)
x = g.community_fastgreedy()

# http://igraph.org/python/doc/igraph.GraphBase-class.html

# http://stackoverflow.com/questions/9471906/what-are-the-differences-between-community-detection-algorithms-in-igraph
# edge.betweenness.community
# fastgreedy.community
# walktrap.community
# spinglass.community
# leading.eigenvector.community
# label.propagation.community

# layout = g.layout("kk")
# igraph.plot(g, layout = layout)