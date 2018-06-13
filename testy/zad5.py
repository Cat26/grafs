from collections import defaultdict as dd
import sys

class Graf():
    def __init__(self):
        self.graf = dd(list)
        self.graf_uporzadkowany = dd(list)

    def tworzenie_grafu(self):
        values = []
        with open(sys.argv[1], 'r') as inFile:#sys.argv[1]
            for line in inFile:
                l = line.replace('{}', '').split()
                for key, val in zip(*[iter(l)]*2):
                    values.append(int(val))
                    self.graf[int(key)].append(int(val))
                    self.graf[int(val)].append(int(key))
            inFile.close()
        for key in range(1, max(values) + 1):
            if key in self.graf.keys():
                self.graf_uporzadkowany[key] = self.graf[key]
            else:
                self.graf_uporzadkowany[key]
        return self.graf_uporzadkowany

    def metoda_dfs(self, start, sciezka=[]):
        sciezka=sciezka+[start]
        for wierzcholek in self.graf_uporzadkowany[start]:
            if not wierzcholek in sciezka:
                sciezka= self.metoda_dfs(wierzcholek, sciezka)
        return sciezka

    def spojnosc_grafu(self, start):
        if len(self.metoda_dfs(start)) < len(self.graf_uporzadkowany.keys()):
            return False
        else:
            return True

    def kwadrat_grafu(self, g, poczatek):# zmodyfikowany tylko dla wierzcholka poczadkowego
        graf_kwadrat = dd(list)
        for w in g:
            for val in g[w]:
                graf_kwadrat[w].append(val)# najpierw kopia grafu
        for wierzcholek in g[poczatek]:# sasiedzi
            for w2 in g[wierzcholek]: # siesiedzi sasiadow
                if w2 not in g[poczatek] and w2 != poczatek: #nie dublujemy krawedzi
                    graf_kwadrat[poczatek].append(w2)
        return graf_kwadrat

    def sciezki(self, poczatek):
        sciezki_do_wierzcholkow = dd()
        lista_odwiedzonych = []
        for wierzcholek in self.graf_uporzadkowany:
            if wierzcholek != poczatek:
                sciezki_do_wierzcholkow[wierzcholek] = 0
        graf = self.graf_uporzadkowany
        while len(lista_odwiedzonych) + 1 != len(self.graf_uporzadkowany.keys()):
            for w in sciezki_do_wierzcholkow:
                if w not in lista_odwiedzonych:
                    sciezki_do_wierzcholkow[w] += 1# zwiekasza o jeden sciezke do nieodwiedzonych jescze wierzcholkow
            for w in graf[poczatek]:
                if w not in lista_odwiedzonych:
                    lista_odwiedzonych.append(w)
            graf = self.kwadrat_grafu(graf, poczatek)# zmiana grafu na jedo kwadrat
        return sciezki_do_wierzcholkow

    def najwieksza_sciezka(self, sciezki):
        return max(sciezki.values())

    def srednica(self):
        max_dla_w = dd()
        for wierzcholek in self.graf_uporzadkowany:
            max_dla_w[wierzcholek] = self.najwieksza_sciezka(self.sciezki(wierzcholek))
        srednica = max(max_dla_w.values())
        return srednica


    def __str__(self):
        return "%s" % self.graf_uporzadkowany


g = Graf()
g.tworzenie_grafu()
# print(g.__str__())
if g.spojnosc_grafu(1) == True:
    print((g.srednica()))
else:
    print('graf niespojny')