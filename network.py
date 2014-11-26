import networkx as nx
with open("edgelist.csv") as f:
	next(f) # skip header
	G=nx.read_edgelist(f, delimiter=",", nodetype=long)

print nx.info(G)

