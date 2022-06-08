# Algorithm to compute Z_q(G) for an arbitrary graph

# Algorithm comes from "Using Variants of Zero Forcing to Bound the Inertia Set of a Graph" by S. Butler, J. Grout, and H. Tracy Hall

import networkx as nx
import copy
import itertools
import math

def force(graph: nx.Graph, blue_vertices: frozenset):
    """Returns a list of the blue vertices after performing Rule 2 on the entire graph"""
    new_blue_vertices = list(blue_vertices)
    for blue_vertex in blue_vertices:
        white_neighbors = frozenset(set(graph.neighbors(blue_vertex)) - set(blue_vertices))
        if len(white_neighbors) == 1 and list(white_neighbors)[0] not in new_blue_vertices:
            new_blue_vertices.append(list(white_neighbors)[0])
    if frozenset(new_blue_vertices) == frozenset(blue_vertices):
        return frozenset(new_blue_vertices)
    else:
        return force(graph, new_blue_vertices)

def calculate_zq(graph: nx.Graph, q):
    # TODO: implement functionality from algorithm
    V = frozenset(graph.nodes)
    cost = {}
    cost[V] = 0
    for i in range(len(V)-1, -1, -1):
        # print("i=", i)
        for U in itertools.combinations(V, i):
            U = frozenset(U)
            if force(graph, U) != U: continue
            # print('  U=', U)
            # print('  forced:', force(graph, U))
            b = math.inf
            c = math.inf
            cost[U] = math.inf
            white_vertices = graph.subgraph([vertex for vertex in graph.nodes if vertex not in U])
            K = [comp for comp in nx.connected_components(white_vertices)]
            # print("  K:", K)

            for J in itertools.combinations(K, q+1):
                b_prime = -math.inf
                for size_I in range(1, q+2):
                    for I in itertools.combinations(J, size_I):
                        I = set.union(*I)
                        # print("    J:", J, "| I:", I)
                        induced_graph = nx.induced_subgraph(graph, set.union(set(U), I))
                        # print("    G[U u I]:", induced_graph.nodes)
                        b_prime = max(b_prime, cost[force(graph, force(induced_graph, U))])
                b = min(b, b_prime)
            
            for v in V-U:
                c = min(c, cost[force(graph, set.union(set(U), {v}))]+1)
            cost[U] = min(b, c)
            # print("cost:", cost)

    return cost[frozenset()]



star_5 = nx.star_graph(4)
# print(star_5)
# print(calculate_zq(star_5, 0))

# print(force(star_5, [2]))
print(calculate_zq(star_5, 1))


# for q in range(0, 8):
#     print("q=" + str(q))
#     for n in range(1, 8):
#         star = nx.star_graph(n-1)
#         print(n, ":", calculate_zq(star, q))
#     print()

for q in range(0, 5):
    print("q=" + str(q))
    for k in range(1, 5):
        for n in range(3, 6):
            if k*n <= 12: # Reduce computation time
                graph = nx.Graph()
                for _ in range(k):
                    star = nx.star_graph(n-1)
                    graph = nx.disjoint_union(graph, star)
                print('k:', k, '| n:', n, ":", calculate_zq(graph, q))
    print()
