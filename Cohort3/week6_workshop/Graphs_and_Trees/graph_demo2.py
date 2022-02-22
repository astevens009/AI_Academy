"""
Accessing the elements of a graph
"""

import networkx as nx

# region Example 1

graph1 = nx.Graph()

graph1.add_edges_from([(1, 2), (1, 3), (3, 4), (3, 5)])

print("\nAccessing Graph Elements\n")
print("=" * 30)
print("\nNODES\n{}".format(graph1.nodes))
print("EDGES\n{}".format(graph1.edges))
print("ADJACENCY LIST\n{}".format(graph1.adj))
print("DEGREE\n{}\n".format(graph1.degree))


print("\nAdjanceny list for node 3\n{}".format(graph1.adj[3]))
print("\nAdjanceny list for node 4\n{}".format(graph1.adj[4]))

print("\nDegree for node 1\n{}".format(graph1.degree[1]))
print("\nDegree for node 4\n{}".format(graph1.degree[4]))

print("\nNodes with a degree of 1:")
for node in graph1.degree:
    if node[1] == 1:
        print(node[0])

# endregion Example 1

# region Example 2



# endregion Example 2