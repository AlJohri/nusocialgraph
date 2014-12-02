import json
from colors import colors, hex_to_rgb, rgbs

# http://igraph.org/python/doc/igraph.GraphBase-class.html

import igraph
g = igraph.Graph.Read_Ncol('edgelist_cultural.txt', directed=False)

mapping = {}
with open("nodes_cultural.txt") as f:
	for row in f.read().splitlines():
		mapping[row.split()[0]] = row.decode('utf-8', 'ignore').encode('ascii', 'ignore')

# Read_Edgelist
igraph.summary(g)
g.simplify()
igraph.summary(g)
# http://stackoverflow.com/questions/9471906/what-are-the-differences-between-community-detection-algorithms-in-igraph
# comms = g.community_edge_betweenness(directed=False).as_clustering()
# comms = g.community_fastgreedy().as_clustering()
comms = g.community_infomap()
# comms = g.community_label_propagation().as_clustering()
# comms = g.community_leading_eigenvector().as_clustering()
# comms = g.community_multilevel() # louvain
# comms = g.community_optimal_modularity().as_clustering()
# comms = g.community_spinglass().as_clustering()
# comms = g.community_walktrap().as_clustering()

pos = g.layout_grid_fruchterman_reingold()

for i in range(len(comms)):
	for n in comms[i]:
		g.vs[n]['viz'] = str({'color': rgbs[i], 'position':{'x':pos[n][0], 'y':pos[n][1]}})
		g.vs[n]['uid'] = g.vs[n]['name']
		g.vs[n]['label'] = mapping[g.vs[n]['uid']]

g.write_gml(open("graph.gml", "w"))
# convert to gefx from gml using networkx

from networkx import nx
G = nx.read_gml('graph.gml')
for node in G.nodes(data=True):
	node[1]['viz'] = eval(node[1]['viz'])
nx.write_gexf(G, './network/data/facebook.gexf')

print "python -m SimpleHTTPServer"
print "http://localhost:8000/network/?config=config_fb.json"
