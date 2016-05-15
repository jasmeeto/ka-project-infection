import networkx as nx
from collections import deque, OrderedDict


def pick_source(g):
    # TODO choose source with centrality
    return g.nodes()[0]

def total_infection(g, source=None):
    infected = OrderedDict()
    for node in g.nodes():
        infected[node] = False

    if source:
        edges_generator = nx.bfs_edges(g, source)
    else:
        source = pick_source(g)
        edges_generator = nx.bfs_edges(g, source)

    iterations = [list(infected.items())]

    g.node[source]['data'].version = 'new'
    infected[source] = True
    iterations.append(list(infected.items()))

    for n1, n2 in edges_generator:
        print n1, n2
        g.node[n2]['data'].version = 'new'
        infected[n2] = True
        iterations.append(list(infected.items()))

    return iterations

# need to implemement custom bfs for threshold
def limited_infection(g, source=None, limit=5, threshold=50):
    if not source:
        source = pick_source(g)

    infected = OrderedDict()
    for node in g.nodes():
        infected[node] = False

    iterations = [list(infected.items())]

    neighbors = g.neighbors_iter
    visited = set()
    queue = deque([source])
    count=0
    while queue:
        if count >= limit:
            break
        n = queue.popleft()
        user = g.node[n]['data'] 
        print user
        if n not in visited:
            print 'infecting...' + str(user)
            user.version = 'new'
            infected[n] = True
            iterations.append(list(infected.items()))
            count+=1
            visited.add(n)

            #weights = [g[n][adj]['weight'] for adj in g.neighbors(n)]
            #avgweight = sum(weights, 0.0) / len(weights)
            for adj in g.neighbors(n):
                if g[n][adj]['weight'] > threshold:
                    queue.append(adj)

        if not queue and count < limit:

    import sys
    sys.stdout.flush()

    return iterations

