# heard of mackenna's gold?? :D go till the end, visit each and every adjacent node of the current node

#NOTE : Thanks Geeksforgeeks.org 

# Depth First search is an algorithm for searching or traversing through the graph starting from the root
# or any arbitrary node until none of the node is unvisited. 

# In simple words LEAVE NO STONES UNTURNED :P 
#ALGO : 
# Take a root node. 
# Mark the node as visited 
# Look for the adjacent nodes(nodes that passes through the current node or so callled the edges of the node), visit each of the 
# edges recursively till the end
# go to the next node and do the same

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)
    

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.DFS(1)