# -*-coding:utf-8-*-
def wierzcholki():
    wierzchołki = int(input("podaj liczbę wierzchołków: "))
    if wierzchołki <= 0:
        print('liczba wierzcholkow musi byc wieksza od zera')
        wierzchołki = wierzcholki()
    return wierzchołki


def lista_sasiedztwa(v):
    graf ={}
    for i in range(1, v+1):
        graf.update({i: []})
        #print('{}: {}'.format(i, graf[i]))
    return graf

def tworzenie_krawedzi(x):
    for i in x:
        print("podaj liste sasiedztwa dla wierzcholka {} jak skonczysz wpisz 0:".format(i))
        krawedz=1
        while krawedz is not 0:
            krawedz = int(input())
            warunek = testy_krawedz(krawedz, x, i)
            if warunek:
                if krawedz != 0:
                    x[i].append(krawedz)
            if warunek == False:
                krawedz = 1
    return x

def testy_krawedz(k,l,i):
    x = len(l)
    if k < 0:
        print('nie ma takiego wierzcholka')
        p = False
    elif k > x:
        print('nie ma takiego wierzcholka')
        p = False
    elif k == i:
        print('w grafie prostym nie moze byc petli')
        p = False
    elif k in l[i]:
        print('krawedz zostala podana wczesniej')
        p = False
    elif k < i and k != 0:
            if i not in l[k]:
                print("nie moze byc takiej krawedzi bo nie zostala uwzgledniona dla wierzcholka {}".format(k))
                p = False
            else:
                p = True
    elif k == 0:
        wykroczenie = []
        for element in l:
            if element < i:
                if i in l[element] and element not in l[i]:
                    print('nie mozna zakonczyc lista musi posiadac wierzcholek nr {}'.format(element))
                    wykroczenie.append(1)
        if sum(wykroczenie)> 0:
            p = False
        else:
            p = True


    else:
        p = True
    return p

def stopien_wierzcholkow(g):
    lista = []
    for key in g:
        lista.append(len(g[key]))
    return sorted(lista, reverse=True)

def stopien_grafu(l):
    return max(l)


if __name__ == "__main__":
    g = (tworzenie_krawedzi(lista_sasiedztwa(wierzcholki())))
    print(g)
    l = stopien_wierzcholkow(g)
    print('stopien wierzcholkow:')
    print(stopien_wierzcholkow(g))
    print('stopien grafu:')
    print(stopien_grafu(l))
