class Node:
    def __init__(self, key):
        self.upward = None
        self.downward = None
        self.val = key

def minValue(node):
    current = node

    while(current.downward is not None):
        current = current.downward

    return current.val

root = Node(60)
root.upward = Node(50)
root.downward = Node(20)
root.upward.upward = Node(3)

print("Nilai terkecil dalam pohon biner adalah", minValue(root))


class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbour):  
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def show_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print("Edge : Node = ", node, " Neighbour = ", neighbour)

g = Graph()
g.addEdge('A', 'B')
g.addEdge('B', 'C')
g.addEdge('A', 'C')
g.addEdge('D', 'E')
g.addEdge('E', 'F')
g.addEdge('F', 'D')

print("Edges of graph:")
g.show_edges()