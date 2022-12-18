# graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

    def get(self, node):
        return self.edges[node]


if __name__ == "__main__":
    G = Graph()
    G.add_node('a')
    G.add_node('b')
    G.add_node('c')
    G.add_node('d')
    G.add_node('e')

    G.add_edge('a', 'b', 1)
    G.add_edge('a', 'c', 2)
    G.add_edge('a', 'd', 3)
    G.add_edge('a', 'e', 4)
    G.add_edge('b', 'c', 5)
    G.add_edge('b', 'd', 6)
    G.add_edge('b', 'e', 7)
    G.add_edge('c', 'd', 8)
    G.add_edge('c', 'e', 9)
    G.add_edge('d', 'e', 10)

    print(G.nodes)
    print(G.edges)
    print(G.distances)


