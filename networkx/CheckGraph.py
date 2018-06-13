import networkx as nx
from networkx import is_tree, is_bipartite, find_cycle

G = nx.Graph()

list_node = [x for x in range(0, 6)] #ilosc wierzcholkow
list_edges = [(0, 3), (4, 0), (1, 3), (1, 5), (4, 2), (5, 2)] #krawedzie

G.add_nodes_from(list_node)
G.add_edges_from(list_edges)

G2 = nx.complete_graph(len(G.nodes))

if is_tree(G):
    print('Graf jest drzewem')
else:
    print ('Graf nie jest drzewem')

if G2.number_of_edges() == G.number_of_edges():# porowanie ilosci krawedzi dla grafu pelnego
    print('Graf jest pelny')
else:
    print('Graf nie jest pelny')

if is_bipartite(G):
    print('Graf jest dwudzielny')
else:
    print('Graf nie jest dwudzielny')

try:
    find_cycle(G, orientation='ignore')
    print('Graf ma cykl')
except:
   print('Graf nie ma cyklu')
