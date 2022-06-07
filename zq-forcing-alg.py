# Algorithm to compute Z_q(G) for an arbitrary graph

# Algorithm comes from "Using Variants of Zero Forcing to Bound the Inertia Set of a Graph" by S. Butler, J. Grout, and H. Tracy Hall

import networkx as nx
import copy

def force(graph: nx.Graph, blue_vertices: list):
    """Returns a list of the blue vertices after performing Rule 2 on the entire graph"""
    new_blue_vertices = copy.copy(blue_vertices)
    for blue_vertex in blue_vertices:
        white_neighbors = list(set(graph.neighbors(blue_vertex)) - set(blue_vertices))
        if len(white_neighbors) == 1:
            new_blue_vertices.append(white_neighbors[0])
    if new_blue_vertices == blue_vertices:
        return new_blue_vertices
    else:
        return force(graph, new_blue_vertices)

def calculate_zq(graph: nx.Graph, q):
    # TODO: implement functionality from algorithm
    V = graph.nodes
    for i in range(len(V)-1, -1, -1):
        pass
    return V



star_5 = nx.star_graph(4)
print(calculate_zq(star_5, 0))

print(force(star_5, [2]))