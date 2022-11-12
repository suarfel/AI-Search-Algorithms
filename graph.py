class Node:
    def __init__(self, data,latitude,longtiude):
        self.data = data
        self.latitude = latitude
        self.longtiude = longtiude

class Edge:
    def __init__(self, left, right,cost):
        self.left = left
        self.right = right
        self.cost = cost

class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.adjacentNodes = {}
    def add_edge(self, left, right,cost):
        if left not in self.nodes:
            self.nodes.append(left)
            self.adjacentNodes[left] = set([])
        if right not in self.nodes:
            self.nodes.append(right)
            self.adjacentNodes[right] = set([])
        edge = Edge(left,right ,cost)
        self.edges[(edge.left,edge.right)] = edge.cost
        self.edges[(edge.right,edge.left)] = edge.cost
        self.adjacentNodes[left].add(right)
        self.adjacentNodes[right].add(left)