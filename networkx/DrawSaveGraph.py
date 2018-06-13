import networkx as nx 
import matplotlib.pyplot as plt
import scipy as sp

G = nx.Graph()

list_node = [x for x in range(0, 6)] #ilosc wierzcholkow
list_edges = [(0, 3), (4, 0), (1, 3), (1, 5), (4, 2), (5, 2)] #krawedzie

G.add_nodes_from(list_node)
G.add_edges_from(list_edges)

plt.figure(1, figsize=(2,2))
nx.draw(G, node_size=10)
plt.show()

A = nx.adjacency_matrix(G)
A_format = A.todense()


with open('macierz_sasiedztwa.txt', 'w') as f:
    for line in A_format:
        line = str(line)
        f.write(line.strip('[').strip(']'))
        f.write('\n')

B = nx.generate_adjlist(G)
with open('lista_sasiedztwa.txt', 'w') as my_file:
    for line in B:
        my_file.write(str(line))
        my_file.write('\n')
