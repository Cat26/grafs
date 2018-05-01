from collections import defaultdict as dd

class Graf():
    def __init__(self):
        self.graf = dd(list)

    def tworzenie_grafu(self):
        inFile = open("graf.txt", 'r')
        for line in inFile:
            (key, val) = line.split(':')
            for char in val.split(','):
                if char != '\n' and char != ',':
                    self.graf[int(key)].append(int(char))
        return self.graf

    def metoda_dfs(self, start, sciezka=[]):
        sciezka=sciezka+[start]
        for wierzcholek in self.graf[start]:
            if not wierzcholek in sciezka:
                sciezka= self.metoda_dfs(wierzcholek, sciezka)
        return sciezka

    def spojnosc_grafu(self,start):
        if len(self.metoda_dfs(start))< len(self.graf.keys()):
            return False
        else:
            return True
    def stopien_wierzcholkow(self):
        stopien=[]
        for wierzcholek in self.graf:
            stopien.append(len(self.graf[wierzcholek]))
        return stopien

    def istnienie_sciezki_lub_cyklu_Eulera(self, start):
        euler = 'graf nie jest eulerowski'
        ilosc_wierzcholkow = len(self.graf.keys())
        if self.spojnosc_grafu(start):
            parzystosc = []
            for stopien in self.stopien_wierzcholkow():
                parzysty = 1
                if stopien % 2 == 0:
                    parzystosc.append(parzysty)
            if len(parzystosc)==ilosc_wierzcholkow:
                euler = 'graf jest eulerowski'
            elif sum(parzystosc)== (ilosc_wierzcholkow-2):
                euler = 'graf jest poleulerowski'
        return euler

    def cykl_eulera(self, start, stos=[]):
        stos.append(start)
        if len(self.graf[start]) == 1:
            new_start = self.graf[start][0]
            self.graf[self.graf[start][0]].remove(start)
            del self.graf[start]
            #print(self.graf)
            start = new_start
            self.cykl_eulera(new_start, stos)
        elif len(self.graf[start]) > 1:
            new_start = self.graf[start][0]
            self.graf[self.graf[start][0]].remove(start)
            self.graf[start].remove(self.graf[start][0])
            #print(self.graf)
            start = new_start
            self.cykl_eulera(start, stos)
        return stos

    def sciezka_eulera(self):
        stopnie = self.stopien_wierzcholkow()
        for s in stopnie:
            if s %2 != 0:
                start = s
        return self.cykl_eulera(start)






g = Graf()
print(g.tworzenie_grafu())
if g.spojnosc_grafu(1):
    print('graf spojny')
else:
    print('graf nie spojny')
#print(g.stopien_wierzcholkow())
e =g.istnienie_sciezki_lub_cyklu_Eulera(1)
print(e)
if e == 'graf jest eulerowski':
    print('sciezka eulera:{}'.format(g.cykl_eulera(1)))
elif e == 'graf jest poleulerowski':
    print('sciezka eulara:{}'.format(g.sciezka_eulera()))