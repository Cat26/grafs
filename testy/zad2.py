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
                l = line.replace('{}','').split()
                for key, val in zip(*[iter(l)]*2):
                    values.append(int(val))
                    self.graf[int(key)].append(int(val))
                    self.graf[int(val)].append(int(key))
            inFile.close()
        for key in range(1,max(values)+ 1):
            if key in self.graf.keys():
                self.graf_uporzadkowany[key]= self.graf[key]
            else:
                self.graf_uporzadkowany[key]
        return self.graf_uporzadkowany

    def __str__(self):
        return "%s" % self.graf_uporzadkowany

    def dopelnienie(self):
        dopelnienie = dd(list)
        lista_wierzcholkow = self.graf_uporzadkowany.keys()
        for wierzcholek in self.graf_uporzadkowany:
            for w in lista_wierzcholkow:
                if w not in self.graf_uporzadkowany[wierzcholek]and wierzcholek != w:
                  dopelnienie[wierzcholek].append(w)
        return dopelnienie

g = Graf()
g.tworzenie_grafu()
# print(g.__str__())
print(g.dopelnienie())