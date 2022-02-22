from collections import defaultdict
from sqlalchemy import null

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
        visited_queue = []
        BFS_queue = []
 
        BFS_queue.append(s)
        visited_queue.append(s)

        while BFS_queue:
            # Alternatively visited_queue.append(BFS_queue.pop(0))
            s = BFS_queue.pop(0)
            s_parent = s.get_node_parent()

            if s_parent == "ROOT":
                print ("{}, Parent: {}".format(s.get_node_value(), s_parent))
            else:
                print ("{}, Parent: {}".format(s.get_node_value(), s_parent.get_node_value()))
 
            for i in self.graph[s]:
                if i not in visited_queue:
                    BFS_queue.append(i)
                    visited_queue.append(i)


class Node:
    def __init__(self, value, parent):
        self.__value = value
        self.__parent = parent

    def __str__(self):
        # TODO: Parent is a node, so you need to access the value of the parent node
        node_info = f"Parent: {self.__parent}\nValue: {self.__value}\n"

        return node_info

    def set_node_value(self, value):
        self.__value = value

    def set_node_parent(self, parent):
        self.__parent = parent

    def get_node_value(self):
        return self.__value

    def get_node_parent(self):
        if self.__parent == null:
            return "ROOT"
        else:
            return self.__parent




if __name__ == '__main__':
    # NOTE: If parent == null then the node is the root
    nodeA = Node('A', null)
    nodeB = Node('B', nodeA)
    nodeC = Node('C', nodeA)
    nodeD = Node('D', nodeA)
    nodeE = Node('E', nodeB)
    nodeF = Node('F', nodeB)
    nodeG = Node('G', nodeC)
    nodeH = Node('H', nodeD)
    nodeI = Node('I', nodeD)

    
    graph_demo = Graph()

    graph_demo.addEdge(nodeA, nodeB)
    graph_demo.addEdge(nodeA, nodeC)
    graph_demo.addEdge(nodeA, nodeD)
    graph_demo.addEdge(nodeB, nodeE)
    graph_demo.addEdge(nodeB, nodeF)
    graph_demo.addEdge(nodeC, nodeG)
    graph_demo.addEdge(nodeD, nodeH)
    graph_demo.addEdge(nodeD, nodeI)

    start_node = nodeA

    print (f"Breadth First Tree Traversal (starting from node {start_node})")
    graph_demo.BFS(start_node)

    print()