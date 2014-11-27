import json
import matplotlib.pyplot as plt
import community
import networkx as nx
from networkx.readwrite import json_graph

print "Loading network from edglist.csv"

with open("edgelist_user.txt") as f:
	G=nx.read_edgelist(f, nodetype=long)

print "Calculating number of nodes, edges, and degree"

print nx.info(G)

# Find largest connected component subgraph
print "Finding largest connected component subgraph"

subgraphs = [sg for sg in nx.connected_component_subgraphs(G)]
print [len(sg) for sg in subgraphs]
sg = subgraphs[0]

print "Calculating number of nodes, edges, and degree"

print nx.info(sg)

# for n in sg:
#     sg.node[n]['name'] = n
# d = json_graph.node_link_data(sg)

# json.dump(d, open('force.json','w'))
# nx.write_dot(sg, 'data.dot')

# print nx.radius(sg)
# print nx.diameter(sg)
# print nx.algorithms.distance_measures.center(G)

part = community.best_partition(sg)
values = [part.get(node) for node in sg.nodes()]

nx.draw_spring(sg, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show()
