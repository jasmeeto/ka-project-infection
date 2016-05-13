import networkx as nx

def total_infection(g, source=None):
	if source:
		edges_generator	= nx.bfs_edges(g, source)
	else:
		# TODO choose source with centrality
		source = source
		edges_generator	= nx.bfs_edges(g, source)

	for e in edges_generator:
		print e
		if e[0] != source:
			g.node[e[0]]['data'].version = 'new'
		if e[1] != source:
			g.node[e[1]]['data'].version = 'new'



