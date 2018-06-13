import networkx as nx
G = nx.Graph()

edges =[(6, 2), (2, 1), (2, 3), (3, 1), (3, 4), (1, 4), (4, 0), (1, 0), (7, 4), (7, 1), (7, 0), (7, 5), (5, 4), (0, 5)]
G.add_edges_from(edges)

print('liczba wierzcholkow: ', G.number_of_nodes())
print('liczba krawedzi: ', G.number_of_edges())
print('stopnie wierzcholkow:')
for w in sorted(G.nodes()):
    print(w, ':', G.degree(w))

print('liczba lisci w grafie: ', len([x for x in G.nodes() if G.degree(x) == 1]))
print('liczba wierzcholkow stopnia 3 : ', len([x for x in G.nodes() if G.degree(x) == 3]))