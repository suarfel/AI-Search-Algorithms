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
# graph loader 
def build_graph(file):
    graph = Graph()
    nodes = {}
    file = open(file)
    for line in file:
        line =line.split(' ')  # this function performs to split one line text  with the spaces in to the list
# creating nodes with given line list.
        left = Node(line[0],float(line[1]),float(line[2])) 
        right = Node(line[3],float(line[4]),float(line[5]))
        weight = int(line[6])
# The two consecutive if else statements are used to check  wheather left and right node is already created nodes in the nodes
        if left.data not in nodes:
            nodes[left.data]  = left
        else:
            left = nodes[left.data]
        if right.data not in nodes:
            nodes[right.data] = right
        else:
            right = nodes[right.data]
        graph.add_edge(left,right,weight)

##### you can check the loader by decomment the below code #######
    for i in  graph.nodes:
        print("the fontiers of ===> ",i.data)
        for j in graph.adjacentNodes[i]:
            print(j.data)


build_graph("Orignal_twenty_node.txt")