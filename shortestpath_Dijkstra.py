from shortestPathFloyed import Node, Edge
from minSpanningTree import list2minheap

INFINITY = 10000

class Graph:
    def __init__(self):
        self._nodeList = []
        self._edgeList = []

    def buildGraph(self):
        for i in range(5):
            self._nodeList.append(Node(i))

        self._edgeList.append(Edge(0, 10, self._nodeList[0], self._nodeList[1]))
        self._edgeList.append(Edge(1, 5, self._nodeList[0], self._nodeList[2]))
        self._edgeList.append(Edge(2, 1, self._nodeList[1], self._nodeList[3]))
        self._edgeList.append(Edge(3, 10, self._nodeList[1], self._nodeList[2]))
        self._edgeList.append(Edge(4, 9, self._nodeList[2], self._nodeList[3]))
        self._edgeList.append(Edge(5, 2, self._nodeList[2], self._nodeList[4]))
        self._edgeList.append(Edge(6, 3, self._nodeList[2], self._nodeList[1]))
        self._edgeList.append(Edge(7, 4, self._nodeList[3], self._nodeList[4]))
        self._edgeList.append(Edge(8, 7, self._nodeList[4], self._nodeList[0]))
        self._edgeList.append(Edge(9, 6, self._nodeList[4], self._nodeList[3]))

    def getVertex(self): return self._nodeList
    def getEdge(self): return self._edgeList

    def graph_print(self):
        for i in range(len(self._edgeList)):
            self._edgeList[i].print()

    def get_edge_Weight(self, u, v):
        for i in range(len(self._edgeList)):
            if self._edgeList[i].getstartNode() == u and self._edgeList[i].getendNode() == v:
                return self._edgeList[i].getDistance()

def INITIALIZE_SINGLE_SOURCE(graph, startNode):
    for each_vertex in graph.getVertex():
        each_vertex.setDistance(INFINITY)
        each_vertex.setPrevNode(None)
    startNode.setDistance(0)


# w 要能对应edgeslist里面的weight
def RELAX(node_u, node_v, w):
    if node_v.getDistance() > node_u.getDistance() + w:
        node_v.setDistance(node_u.getDistance() + w)
        node_v.setPrevNode(node_u)


def EXTRACT_MIN(Q):  # Q is a nodelist
    weight_list = list2minheap([Q[i].getDistance() for i in range(len(Q))])
    smallest = weight_list.HEAP_MINIMUM()

    for i in range(len(Q)):
        if smallest == Q[i].getDistance():
            selected_node = Q[i]
            Q.pop(i)
            break
    return selected_node, Q

def DijkstraAlgo(graph, startNode):
    INITIALIZE_SINGLE_SOURCE(graph, startNode)
    S = []
    Q = graph.getVertex()
    while len(Q) != 0:
        smallest_node, Q = EXTRACT_MIN(Q)
        S.append(smallest_node)
        for each_vertex in smallest_node.getAdjNodeList():
            RELAX(smallest_node, each_vertex,
                  graph.get_edge_Weight(smallest_node,each_vertex))
    return S

test_graph = Graph()
test_graph.buildGraph()
print("*************Before DIJKSTRA**************")
test_graph.graph_print()
print("*************After DIJKSTRA***************")

startNode = test_graph.getVertex()[0]
nodes = DijkstraAlgo(test_graph, startNode)
nodes.sort(key = lambda x: x.getId())
for i in range(len(nodes)):
    print("Node ", startNode.getId(), "-->", nodes[i].getId(), " ", nodes[i].getDistance())






