# Napisz program, który sprawdzi czy podany graf jest:
# - Drzewem
# - Cyklem C_n
# - Grafem pełnym K_n
# - Grafem k-regularnym
from collections import defaultdict as dd

class Graf():
    def __init__(self, wierzcholki):
        self.graf = dd(list)
        self.W = wierzcholki

    def dodaj_krawedz(self, w1, w2):
        self.graf[w1].append(w2)
        self.graf[w2].append(w1)

    def stopien_wierzcholkow(self):
        lista = []
        for key in self.graf:
            lista.append(len(self.graf[key]))
        return sorted(lista, reverse=True)

    def liczba_krawedzi(self):
        return sum(self.stopien_wierzcholkow())/2

    def czy_pelny(self):
        pelny = True
        for wierzcholek in self.graf:
            if len(self.graf[wierzcholek]) != self.W - 1:
                pelny = False
        return pelny

    def cykliczny_pomocniczy(self, w, odwiedzony, stos):
        odwiedzony[w] = True
        stos[w] = True
        for w_sasiedni in self.graf[w]:
            if odwiedzony[w_sasiedni] == False:
                if self.cykliczny_pomocniczy(w_sasiedni, odwiedzony, stos) == True:
                    return True
            elif stos[w_sasiedni] == True:
                return True

        stos[w] = False
        return False


    def czy_cykliczny(self):
        odwiedzony = [False] * self.W
        stos = [False] * self.W
        for wierzcholek in range(self.W):
            if odwiedzony[wierzcholek] == False:
                if self.cykliczny_pomocniczy(wierzcholek, odwiedzony, stos) == True:
                    return True
        return False

    def metoda_dfs(self, start, sciezka=[]):
        sciezka=sciezka+[start]
        for wierzcholek in self.graf[start]:
            if not wierzcholek in sciezka:
                sciezka= self.metoda_dfs(wierzcholek, sciezka)
        return sciezka

    def czy_drzewo(self):
        drzewo = True
        if len(self.metoda_dfs(1)) != len(self.graf):
            drzewo = False
        elif self.czy_cykliczny() == False:
            drzewo = False
        elif len(self.graf) != self.liczba_krawedzi() + 1:
            drzewo = False
        return drzewo

    def czy_regularny(self):
        regularny = True
        reg = len(self.graf[0])
        for i in self.graf:
            reg != self.graf[i]
            regularny = False
        return regularny




g = Graf(4)
g.dodaj_krawedz(0, 1)
g.dodaj_krawedz(0, 2)
g.dodaj_krawedz(0, 3)
g.dodaj_krawedz(0, 4)


print(g.graf)
if g.czy_cykliczny():
    print("graf  nie jest cykliczny")

else:
    print("graf jest cykliczny")

if g.czy_pelny():
    print("graf jest pelny")

else:
    print("graf nie jest pelny")


if g.czy_regularny():
    print("graf jest regularny")

else:
    print("graf nie jest regularny")


if g.czy_drzewo():
    print("graf jest drzewem")

else:
    print("graf nie jest drzewem")