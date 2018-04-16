from collections import defaultdict as dd

class Graf():
    def __init__(self, wierzcholki):
        self.graf = dd(list)
        self.W = wierzcholki

    def dodaj_krawedz(self, w1, w2):
        self.graf[w1].append(w2)
        self.graf[w2].append(w1)

    def metoda_dfs(self, start, sciezka=[]):
        sciezka=sciezka+[start]
        for wierzcholek in self.graf[start]:
            if not wierzcholek in sciezka:
                sciezka= self.metoda_dfs(wierzcholek, sciezka)
        return sciezka


g = Graf(5)
g.dodaj_krawedz(0, 1)
g.dodaj_krawedz(1, 2)
g.dodaj_krawedz(2, 3)
g.dodaj_krawedz(2, 4)
g.dodaj_krawedz(3, 4)


print(g.metoda_dfs(1))


