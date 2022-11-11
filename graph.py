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