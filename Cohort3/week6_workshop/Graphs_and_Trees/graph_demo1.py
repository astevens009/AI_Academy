import networkx as nx

graph1 = nx.Graph()

# region Creating and displaying nodes

graph1.add_node("Enterprise")
graph1.add_nodes_from(["Enterprise-A", "Enterprise-B", "Enterprise-C", "Enterprise-D"])
# print("\n{}\n".format(graph1.nodes()))

# endregion Creating and displating nodes

# region Adding edges

graph2 = nx.Graph()

# region Example 1

graph1.add_edge("Enterprise", "Enterprise-A")
graph1.add_edge("Enterprise-B", "Enterprise-C")

# print(graph1.edges())

# endregion Example 1

# region Example 2

# NOTE: If nodes aren't specified, they are automatically added
graph2.add_edge(1, 2)
graph2.add_edge(3, 4)

# Adding multiple edges
graph2.add_edges_from([(4, 2), (3, 5), (5, 4)])

# NOTE: These duplicates will be ignored
graph2.add_node(2)
graph2.add_edge(1, 2)

# print("\n{}".format(graph2.nodes()))
# print("{}\n".format(graph2.edges()))

# endregion Example 2

# endregion Adding edges

# region Removing Nodes & Edges
graph3 = nx.Graph()

# region Example 1

graph3.add_edges_from([("Enterprise", "Enterprise-A"), ("Enterprise-B", "Enterprise-D")])
graph3.add_edges_from([("Enterprise-D", "Enterprise-E")])

# print("\nNODES:\n{}".format(graph3.nodes()))
# print("EDGES:\n{}\n".format(graph3.edges()))

# Removing edge
graph3.remove_edge("Enterprise-B", "Enterprise-D")
# print("\nNODES:\n{}".format(graph3.nodes()))
# print("EDGES:\n{}\n".format(graph3.edges()))

# endregion Example 1

# region Example 2
graph4 = nx.Graph()

graph4.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
graph4.add_edges_from([(5, 6), (5, 7), (5, 8), (7, 8)])
print("\nADDING NODES & EDGES...\n{}".format(graph4.nodes()))
print("{}\n".format(graph4.edges()))

# Removing edge 1-2 from graph
graph4.remove_edge(2, 1)

# Removing edge 3-4 and 1-4 at the same time
graph4.remove_edges_from([(3, 4), (1, 4)])

print("\nREMOVING EDGES...")
print("{}".format(graph4.nodes()))
print("{}\n".format(graph4.edges()))

# Removing nodes
graph4.remove_node(5)
graph4.remove_nodes_from([7, 8])

print("\nREMOVING NODES...")
print("{}".format(graph4.nodes()))
print("{}\n".format(graph4.edges()))

# endregion Example 2

# endregion Removing Nodes & Edges


