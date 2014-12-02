#!/usr/bin/python
import networkx as nx
from heapq import heappush, heappop
from operator import itemgetter

def CNM(G):
    """
    Algorithm for finding the community structure my maximizing the Q value.

    "Finding community structure in very large networks" (2004)
    Aaron Causet, M.E.J. Newman, Cristopher Moore

    Returns the following as a tuple:
        <maximum Q value>
        <communities making up the max Q value>
        <dendragram graph>
        <root node in the dendragram graph>
    """

    # find the largest connected component
    ccs = nx.connected_components(G)
    G = G.subgraph(ccs[0])

    if len(G) < 2:
        n = G.nodes()[0]
        G.clear()
        G.add_node((n,))
        return (0,G.nodes(),G,G.nodes()[0])

    # deltaQ
    deltaQ = {}

    # H values
    H = {}

    # the a values
    a = {}

    q = 0
    maxQ = None

    tree = nx.Graph()
    tree.add_nodes_from(((n,) for n in G))

    # m is the number of edges
    m = G.size()

    for node in G:
        dqr = {}
        ki = G.degree(node)

        # assign row values
        for neighbor in G[node]:
            kj = G.degree(neighbor)
            dqr[(neighbor,)] = 2*(1.0/(2 * m) - (ki * kj)/((2.0*m)**2))

        H[(node,)] = max(dqr.iteritems(), key=itemgetter(1))

        deltaQ[(node,)] = dqr

        av = ki/(2.0 * m)
        a[(node,)] = av
        q -= av**2

    # simple function for pulling our structures
    def embeddedkey(key):
        return key[1][1]

    while len(deltaQ) > 1:

        # find the max H value
        (i, (j,mdq)) = max(H.iteritems(), key=embeddedkey)

        # merge communities i and j
        ci = deltaQ.pop(i)
        cj = deltaQ.pop(j)
        ai = a.pop(i)
        aj = a.pop(j)

        # create a label for our parent node as a joined tuple
        li = i
        lj = j
        label = li + lj

        cij = {}

        marker = {}
        # O( |i| log(n) )
        for key in ci.iterkeys():
            if key == j:
                continue

            del deltaQ[key][i]
            # k is connected to i
            marker[key] = 2

        # O( |j| log(n) )
        for key in cj.iterkeys():
            if key == i:
                continue
            try:
                del deltaQ[key][j]
            except:
                import pdb; pdb.set_trace()
            try:
                # both are conected to k (3)
                marker[key] += 1
            except:
                # k is connected to j
                marker[key] = 1

        for key in marker.iterkeys():
            markerkey = marker[key]
            if markerkey == 3:
                newDeltaQ = ci[key] + cj[key]
            elif markerkey == 2:
                newDeltaQ = ci[key] - (2 * aj * a[key])
            elif markerkey == 1:
                newDeltaQ = cj[key] - (2 * ai * a[key])

            # get the last best maxQ
            (col, maxDeltaQ) = H[key]

            cij[key] = newDeltaQ
            deltaQ[key][label] = newDeltaQ

            if col == j or col == i:
                H[key] = max(deltaQ[key].iteritems(), key=itemgetter(1))

        # cleanup the old stuff
        del H[i]
        del H[j]

        deltaQ[label] = cij
        try:
            H[label] = max(cij.iteritems(), key=itemgetter(1))
        except ValueError:
            pass
        a[label] = ai + aj

        tree.add_node(label)
        tree.add_edges_from([(label,i), (label,j)])

        if not maxQ and mdq < 0:
            maxQ = q
            maxCommunities = H.keys()
        q += mdq

    return (maxQ,maxCommunities,tree,deltaQ.keys()[0])
