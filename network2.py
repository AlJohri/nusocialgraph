import json, os
from colors import colors, hex_to_rgb, rgbs

# http://igraph.org/python/doc/igraph.GraphBase-class.html

KEYWORD = "asian"

if os.path.isfile('edgelist_%s.txt' % KEYWORD): os.remove('edgelist_%s.txt' % KEYWORD)
if os.path.isfile('nodes_%s.txt' % KEYWORD): os.remove('nodes_%s.txt' % KEYWORD)

os.system('make edgelist_%s.txt' % KEYWORD)
os.system('make nodes_%s.txt' % KEYWORD)

import igraph
g = igraph.Graph.Read_Ncol('edgelist_%s.txt' % KEYWORD, directed=False)

mapping = {}
with open('nodes_%s.txt' % KEYWORD) as f:
	for row in f.read().splitlines():
		mapping[row.split()[0]] = row.decode('utf-8', 'ignore').encode('ascii', 'ignore')

# Read_Edgelist
igraph.summary(g)
g.simplify()
igraph.summary(g)
# http://stackoverflow.com/questions/9471906/what-are-the-differences-between-community-detection-algorithms-in-igraph

# comms = g.community_edge_betweenness(directed=False).as_clustering() # TOO SLOW
# comms = g.community_fastgreedy().as_clustering() # 4
comms = g.community_infomap() # 12
# comms = g.community_label_propagation()  # too few communities?
# comms = g.community_leading_eigenvector() # 5
# comms = g.community_multilevel() # louvain, 5
# comms = g.community_optimal_modularity() # too slow?
# comms = g.community_spinglass().as_clustering()
# comms = g.community_walktrap().as_clustering()
print len(comms), "communities found"
print "calculating positions via fruchterman reingold"
pos = g.layout_grid_fruchterman_reingold()

print "setting colors and positions on each node"
for i in range(len(comms)):
	for n in comms[i]:
		color = rgbs[i] if i < len(rgbs) else { "r": 211, "g": 211, "b": 211 }
		if len(comms[i]) < 5: color = { "r": 211, "g": 211, "b": 211 }
		g.vs[n]['viz'] = str({'color': color, 'position':{'x':pos[n][0], 'y':pos[n][1]}})
		g.vs[n]['uid'] = g.vs[n]['name']
		g.vs[n]['label'] = mapping[g.vs[n]['uid']]

print "saving to gml"
g.write_gml(open("graph.gml", "w"))

print "read gml file in networkx"
from networkx import nx
G = nx.read_gml('graph.gml')
for node in G.nodes(data=True):
	node[1]['viz'] = eval(node[1]['viz'])
print "write to gefx from networkx"
nx.write_gexf(G, './network/data/%s.gexf' % KEYWORD)
config = json.load(open("./network/sample.json"))
config['data'] = 'data/%s.gexf' % KEYWORD
json.dump(config, open('./network/%s.json' % KEYWORD, 'w'))

print "done!"