import json
import requests
from collections import defaultdict

import networkx as nx

import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def generate_edges(self, graph):
        edges = []
    
        # for each node in graph
        for node in graph:
            print('::node is ::: ', node)
            
            for neighbour in graph[node]:
                print('::neighbour is ::: ', neighbour)
                
                edges.append((node, neighbour))
        return edges
    
    
    def visualize_graph(self, graph_obj):
        nx.draw(graph_obj)
        plt.savefig("filename.png")


if __name__ == "__main__":
    g = nx.Graph()
    g2 = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    edges = g2.generate_edges(g)
    print('::edges::')
    print(edges)
    #to visualize the graph
    nx.draw(g)
    plt.savefig("filename.png")
