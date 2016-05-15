import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
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

def animate(g, iterations, output_file, use_graphviz=False, is_weighted=False):

    if len(iterations) < 1:
        print "need iterations to animate"
        return

    fig = plt.figure()

    if use_graphviz:
        pos = graphviz_layout(g, prog='neato')
    else:
        pos = nx.spring_layout(g, k=0.20, iterations=100)

    colors = ['R' if is_infected else 'G' for node, is_infected in iterations[0]]
    sizes = [len(v) * 200 for v in g.nodes()]

    def animate(i):
        fig.clear()
        colors = ['R' if is_infected else 'G' for node, is_infected in iterations[i]]
        nx.draw(g, pos=pos, node_size=sizes, node_color=colors, font_size=10, with_labels=True)
        # if is_weighted:
        #     labels = nx.get_edge_attributes(g,'weight')
        #     nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

    ani = animation.FuncAnimation(fig, animate, np.arange(len(iterations)), interval=300)

    if output_file:
        if not output_file.endswith('.mp4'):
            print 'Need to have an mp4 output_file' 
        else: 
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=2, bitrate=1600)
            ani.save(output_file, writer=writer)

    plt.show()
