from collections import defaultdict as dd
import sys

class Graf():
    def __init__(self):
        self.graf = dd(list)
        self.graf_uporzadkowany = dd(list)

    def tworzenie_grafu(self, czy_skierowany):
        values = []
        with open(sys.argv[2], 'r') as inFile:#sys.argv[1]
            for line in inFile:
                l = line.replace('{}','').split()
                for key, val in zip(*[iter(l)]*2):
                    values.append(int(val))
                    self.graf[int(key)].append(int(val))
                    if czy_skierowany == False:
                        self.graf[int(val)].append(int(key))# jak graf nieskierowany dodajemy tez krawedz do drugiego wierzcholka
            inFile.close()
        for key in range(1, max(values) + 1):
            if key in self.graf.keys():
                self.graf_uporzadkowany[key] = self.graf[key]
            else:
                self.graf_uporzadkowany[key]
        return self.graf_uporzadkowany

    def kwadrat_grafu(self):
        graf_kwadrat = dd(list)
        for w in self.graf_uporzadkowany:
            for val in self.graf_uporzadkowany[w]:
                graf_kwadrat[w].append(val)# najpierw kopia grafu
        for wierzcholek in self.graf_uporzadkowany:
            for w1 in self.graf_uporzadkowany[wierzcholek]:# sasiedzi
                for w2 in self.graf_uporzadkowany[w1]: # siesiedzi sasiadow
                    if w2 not in self.graf_uporzadkowany[wierzcholek] and w2 != wierzcholek: #nie dublujemy krawedzi
                        graf_kwadrat[wierzcholek].append(w2)
        return graf_kwadrat

    def __str__(self):
        return "%s" % self.graf_uporzadkowany


g = Graf()
if sys.argv[1] == '-s':
    p = True
if sys.argv[1] == '-n':
    p = False
g.tworzenie_grafu(p)
# print(g.__str__())
print(g.kwadrat_grafu())
