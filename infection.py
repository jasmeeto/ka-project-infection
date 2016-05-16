import sys
import networkx as nx
import numpy as np
from collections import deque, OrderedDict
from pqueue import PriorityQueue

def pick_source(g):
    '''
    Picks source node from graph

    params
    ------
    g: input graph

    returns
    ------
    chosen node
    '''
    return np.random.choice(g.nodes())

def total_infection(g, source=None):
    '''
    Runs total infection using BFS

    params
    ------
    g: input graph
    source: node to start infection from

    returns
    ------
    iterations for animation
    '''

    # create dictionary of nodes to store state for animation
    infected = OrderedDict()
    for node in g.nodes():
        infected[node] = False

    g = g.to_undirected()

    # create generator for iterating on edges of
    # bfs search (created by networkx)
    if source:
        edges_generator = nx.bfs_edges(g, source)
    else:
        source = pick_source(g)
        edges_generator = nx.bfs_edges(g, source)

    # store initial state
    iterations = [list(infected.items())]

    # infect source
    g.node[source]['data'].version = 'new'
    infected[source] = True
    iterations.append(list(infected.items()))

    for n1, n2 in edges_generator:
        print n1, n2
        g.node[n2]['data'].version = 'new'
        infected[n2] = True
        iterations.append(list(infected.items()))

    return iterations

def limited_infection(g, source=None, limit=5, threshold=0):
    '''
    Runs limited infection using adjusted BFS 

    params
    ------
    g: input graph
    source: node to start infection from
    limit: max number of nodes
    threshold: min value of edge weights to traverse on and accept

    returns
    ------
    iterations for animation
    '''
    if not source:
        source = pick_source(g)

    # create dictionary of nodes to store state for animation
    infected = OrderedDict()
    for node in g.nodes():
        infected[node] = False

    # store initial state
    iterations = [list(infected.items())]

    # run altered bfs algorithm
    visited = set()
    queue = PriorityQueue()
    queue.add(source, 1)
    count=0

    while not queue.is_empty():
        # exact if limit reached
        if count >= limit:
            break

        # pop node from priority queue of nodes
        p, n = queue.pop_smallest()
        print (p, n)
        user = g.node[n]['data'] 

        if n not in visited:
            # infect current node
            user.version = 'new'
            infected[n] = True
            iterations.append(list(infected.items()))
            visited.add(n)
            # increment count of infected nodes
            count+=1

            # children of current node not yet infected
            suc = [adj for adj in g.successors(n) if adj not in visited]
            # parents of current node not yet infected
            pre = [adj for adj in g.predecessors(n) if adj not in visited]

            # if there are enough children to be under limit
            # add them with priority 1
            if suc and len(suc) <= (limit - count - queue.size(1)):
                for adj in suc:
                    if g[n][adj]['weight'] > threshold:
                        queue.add(adj, 1) 

            # else add them with priority 2
            else:
                for adj in suc:
                    if g[n][adj]['weight'] > threshold:
                        queue.add(adj, 2) 

            # add parents with priority 3
            for adj in pre:
                if g[adj][n]['weight'] > threshold:
                    queue.add(adj, 3)

            # add all adjacent nodes if nothing in queue
            if queue.is_empty():
                for adj in suc:
                    if g[n][adj]['weight'] > threshold:
                        queue.add(adj, 4)
                for adj in pre:
                    if g[adj][n]['weight'] > threshold:
                        queue.add(adj, 4)

    # flush output for testing
    sys.stdout.flush()

    return iterations

