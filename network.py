import networkx as nx

print "Loading network from edglist.csv"

with open("edgelist.csv") as f:
	next(f) # skip header
	G=nx.read_edgelist(f, delimiter=",", nodetype=long)

print "Calculating number of nodes, edges, and degree"

print nx.info(G)

# Find largest connected component subgraph
print "Finding largest connected component subgraph"

subgraphs = [sg for sg in nx.connected_component_subgraphs(G)]
print [len(sg) for sg in subgraphs]
sg = subgraphs[0]

print "Calculating number of nodes, edges, and degree"

print nx.info(sg)


# print nx.radius(sg)
# print nx.diameter(sg)
# nx.algorithms.distance_measures.center(G)