# -*-coding:utf-8-*-
print("Podaj graf prosty nieskierowany: ")
wierzchołki = int(input("podaj liczbę wierzchołków: "))

if wierzchołki <= 0:
    print(" niepoprawna liczba wierzchołków, musi być co najmniej 1 wierzchołek")
    wierzchołki = int(input("podaj liczbę wierzchołków: "))

krawedzie = int(input("podaj liczbę krawedzi: "))


if krawedzie > wierzchołki*(wierzchołki-1)/2:
    print("za dużo krawędzi, krawędzi może być najwięcej n(n-1)/2")
    krawedzie = int(input("podaj liczbę krawedzi: "))




elif krawedzie < 0:
    print(" niepoprawna liczba krawędzi, liczba musi być nieujemna")
    wierzchołki = int(input("podaj liczbę wierzchołków: "))

macierz = {}

for i in range(1, wierzchołki + 1):
    macierz[i] = []
    for k in range(wierzchołki):
        macierz[i].append(0)


def tworzenie_krawedzi(k,krawedzie):
    for i in range(k,krawedzie+1):
        print('Podaj krawędź nr %s: ' % i)
        w1 = int(input("wierzchołek nr: "))
        w2 = int(input("łączy się z wierzchołkiem nr: "))
        try:
            if w1 == w2:
                print('w grafie prostym nie może być pętli podaj inną krawędź')
                tworzenie_krawedzi(i,krawedzie)
                break
            elif macierz[w1][w2-1] == 1:
                print("w grafie prostym nie może być wielokrotnych krawędzi podaj inną krawędź")
                tworzenie_krawedzi(i, krawedzie)
                break
            else:
                macierz[w1][w2-1]= 1
                macierz[w2][w1-1]= 1
        except IndexError:
            print("niepoprawny nr wierzchołka, możliwe wierzchołki: 1 - %d" % wierzchołki)
            tworzenie_krawedzi(i, krawedzie)
            break
        except KeyError:
            print("niepoprawny nr wierzchołka, możliwe wierzchołki: 1 - %d" % wierzchołki)
            tworzenie_krawedzi(i, krawedzie)
            break
    return macierz


def stopien_wierzcholkow(dict):
    lista = []
    for key in dict:
        lista.append(sum(dict[key]))
    return lista


def stopien_grafu(l):
    return max(l)

tworzenie_krawedzi(1,krawedzie)
l = stopien_wierzcholkow(macierz)
print("stopień wierzchołków: ")
l2 = sorted(l, reverse=True)
print(l2)
print("stopień grafu: %d" % stopien_grafu(l))
