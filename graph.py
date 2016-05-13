import networkx as nx
import matplotlib.pyplot as plt
from user import User

def create_graph(file_name, is_weighted=False):
    g = nx.Graph()
    for line in open(file_name):
        linedata = line.split()
        n1 = linedata[0]
        n2 = linedata[1]
        w = float(linedata[2]) if is_weighted else 1.0
        g.add_node(n1, data=User(n1))
        g.add_node(n2, data=User(n2))
        g.add_edge(n1, n2, weight=w)

    return g

def draw(g):
    colors = ['R' if node[1]['data'].version == 'new' else 'G' for node in g.nodes(data=True)]
    sizes = [len(v) * 200 for v in g.nodes()]
    pos = nx.spring_layout(g, k=0.20, iterations=100)
    nx.draw(g, pos=pos, node_size=sizes, node_color=colors, font_size=10, with_labels=True)
    plt.show()