import json, pickle
import matplotlib.pyplot as plt
from pprint import pprint as pp
import community
import networkx as nx
from networkx.algorithms.approximation.clique import max_clique
from networkx.readwrite import json_graph

print "Loading network from edgelist.csv"

# relabel_nodes
with open("edgelist_al.txt") as f:
	G=nx.read_edgelist(f, nodetype=long)

mapping = {}
with open("nodes_al.txt") as f:
	for row in f.read().splitlines():
		mapping[long(row.split()[0])] = row.decode('utf-8', 'ignore').encode('ascii', 'ignore')

	# " ".join(row.split()[1:])

G = nx.relabel_nodes(G, mapping, copy=True)

print "Calculating number of nodes, edges, and degree"

print nx.info(G)

# Find largest connected component subgraph
# print "Finding largest connected component subgraph"

# subgraphs = [sg for sg in nx.connected_component_subgraphs(G)]
# print [len(sg) for sg in subgraphs]
# G = subgraphs[0]

# print "Calculating number of nodes, edges, and degree"
# print nx.info(G)

# nx.write_gml(sg, 'nu.gml')

colors = [
	'1f77b4',
	'ff7f0e',
	'2ca02c',
	'd62728',
	'9467bd',
	'8c564b',
	'e377c2',
	'7f7f7f',
	'bcbd22',
	'17becf']

def hex_to_rgb():
	cList = []
	for hex_digits in colors:
		rgbDict = {}
		rgb = tuple([int(s, 16) for s in (hex_digits[0:2], hex_digits[2:4], hex_digits[4:6])])
		rgbDict['r'] = rgb[0]
		rgbDict['g'] = rgb[1]
		rgbDict['b'] = rgb[2]
		cList.append(rgbDict)
	return cList

rgbs = [
 {'b': 180, 'g': 119, 'r': 31},
 {'b': 14, 'g': 127, 'r': 255},
 {'b': 44, 'g': 160, 'r': 44},
 {'b': 40, 'g': 39, 'r': 214},
 {'b': 189, 'g': 103, 'r': 148},
 {'b': 75, 'g': 86, 'r': 140},
 {'b': 194, 'g': 119, 'r': 227},
 {'b': 127, 'g': 127, 'r': 127},
 {'b': 34, 'g': 189, 'r': 188},
 {'b': 207, 'g': 190, 'r': 23}]

#Run community detection algorithm
print('Detecting communities...')
myCNM = community.CNM(G)
comms = myCNM[1]
# nx.write_gexf(, './network/data/comm.gexf')
pickle.dump(comms, open("comms.pickle", "wb"))

#Calculate node positions
print('Laying out nodes...')
pos = nx.spring_layout(G, scale = 1000)

print('Saving attributes...')
#Add the visual attrs to each node
for i in range(len(comms)):
	for n in comms[i]:
		G.node[n]['viz']={'color': rgbs[i], 'position':{'x':pos[n][0], 'y':pos[n][1]}}

#Export to 'facebook.gexf'
nx.write_gexf(G, './network/data/facebook.gexf')

# nx.draw_graphviz(sg, prog='sfdp')

# c = max_clique(sg)
# print nx.info(c)

# for n in sg:
#     sg.node[n]['name'] = n
# d = json_graph.node_link_data(sg)

# json.dump(d, open('force.json','w'))
# nx.write_dot(sg, 'data.dot')

# print nx.radius(sg)
# print nx.diameter(sg)
# print nx.algorithms.distance_measures.center(G)

# part = community.best_partition(sg) # part is a dict of the partition for each node
# values = [part.get(node) for node in sg.nodes()]
# nx.draw_spring(sg, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)

# plt.show()
