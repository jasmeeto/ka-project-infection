import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from user import User


def create_graph(file_name, is_weighted=False):
    '''
    Creates graph from file

    params
    ------
    file_name: file to load
    is_weighted: whether or not the graph has weighting info

    returns
    -------
    NetworkX directed graph object (DiGraph)
    '''

    g = nx.DiGraph()
    for line in open(file_name):
        linedata = line.split()
        n1 = linedata[0]
        n2 = linedata[1]
        w = float(linedata[2]) if is_weighted else 1.0
        g.add_node(n1, data=User(n1))
        g.add_node(n2, data=User(n2))
        g.add_edge(n1, n2, weight=w)

    return g

def animate(g, iterations, output_file, use_graphviz=False, is_weighted=False):
    '''
    Animates progression of infection algorithm

    params
    ------
    g: input graph
    iterations: list of state at each iteration of the algorithm
    output_file: file to write animation
    use_graphviz: should use graphviz?
    is_weighted: is a weighted graph

    '''

    if len(iterations) < 1:
        print("need iterations to animate")
        return

    fig = plt.figure(figsize=(10, 7))

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
        # uncomment if weights should be shown on edges
        # looks ugly for large graphs
        # if use_graphviz and is_weighted:
        #     labels = nx.get_edge_attributes(g,'weight')
        #     nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

    ani = animation.FuncAnimation(fig, animate, np.arange(len(iterations)), interval=300)

    if output_file:
        if not output_file.endswith('.mp4'):
            print('Need to have an mp4 output_file')
        else: 
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=2, bitrate=1600)
            ani.save(output_file, writer=writer)

    plt.show()
