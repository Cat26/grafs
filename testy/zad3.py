from collections import defaultdict as dd
import sys

class Graf():
    def __init__(self):
        self.graf = dd(list)
        self.graf_uporzadkowany = dd(list)

    def tworzenie_grafu(self):# metoda tylko dla porownania
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

    def tworzenie_grafu_krawedziowego(self):
        graf_pomocniczy = dd(list)
        graf_krawedziowy = dd(list)
        with open(sys.argv[1], 'r') as inFile:#sys.argv[1]
            for line in inFile:
                l = line.replace('{}','').split()
                for key, val in zip(*[iter(l)]*2):# zeby wziac z calego ciagu tylko dwie liczby
                    graf_pomocniczy[key + '-' + val].append(key)# pomocniczo wstawiamy wierzcholki ktore sie wczesniej laczyly
                    graf_pomocniczy[key + '-' + val].append(val)
            inFile.close()
        for wierzcholek in graf_pomocniczy:
            for element in wierzcholek:# sprawdzamy czy dany wierzcholek wystepuje w innych zeby byly razem 3 iteracja po elementach wczesniejszej krawedzi
                for w in graf_pomocniczy.keys():
                    if w != wierzcholek:# sprawdzamy we wszystkich wierzcholkach
                        if element in graf_pomocniczy[w]:
                            graf_krawedziowy[wierzcholek].append(w)
        return graf_krawedziowy

g = Graf()
print(g.tworzenie_grafu_krawedziowego())