import networkx as nx
import numpy as np
from collections import deque, OrderedDict
from pqueue import PriorityQueue

def pick_source(g):
    return np.random.choice(g.nodes())

def total_infection(g, source=None):
    infected = OrderedDict()
    for node in g.nodes():
        infected[node] = False

    g = g.to_undirected()

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
    # queue = deque([source])
    queue = PriorityQueue()
    queue.add(source, 1)
    count=0
    print limit
    while not queue.is_empty():
        if count >= limit:
            break
        tup = queue.pop_smallest()
        print tup
        p, n = tup
        user = g.node[n]['data'] 
        if n not in visited:
            #print 'infecting...' + str(user)
            user.version = 'new'
            infected[n] = True
            iterations.append(list(infected.items()))
            count+=1
            visited.add(n)

            # weights = [g[n][adj]['weight'] for adj in g.neighbors(n)]
            # avgweight = sum(weights, 0.0) / len(weights)
            suc = [adj for adj in g.successors(n) if adj not in visited]
            pre = [adj for adj in g.predecessors(n) if adj not in visited]
            print len(suc), n
            if suc and len(suc) <= (limit - count - queue.size(1)):
                for adj in suc:
                    queue.add(adj, 1)
                    print 'putting' + str((1,adj))
            for adj in pre:
                queue.add(adj, 2)
                print 'putting' + str((2,adj))

            if queue.is_empty():
                for adj in suc:
                    queue.add(adj, 3)
                for adj in pre:
                    queue.add(adj, 3)



            

    import sys
    sys.stdout.flush()

    return iterations

