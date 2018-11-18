import networkx as nx
import matplotlib.pyplot as plt

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "viewgraph/main.html")

# разбить на 3 функции!!!


def buildgraph(request):
    ipstoip0 = [("ip1", "ip0"), ("ip2", "ip0"), ("ip3", "ip0"), ("ip4", "ip0")]
    ipsout = [("ip0", "ipout")]

    G = nx.Graph()
    for item in ipstoip0:
        G.add_edge(item[0], item[1])
    for item in ipsout:
        G.add_edge(item[0], item[1])

    nx.draw_circular(G,
                     with_labels=True,
                     node_size=200,
                     node_color='r',
                     node_shape='.',
                     font_size=14,
                     font_color='b',
                     font_family='monospace',
                     font_weight='book',
                     horizontalalignment='left',
                     verticalalignment='center'
                     )

    plt.axis('off')
    plt.show()
    plt.savefig('graph.png')
    return render(request, "viewgraph/main.html")
