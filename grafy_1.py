#-*-coding:utf-8-*-
wierzchołki = int(input("podaj liczbę wierzchołków: "))
print("wierzchołki zostały ponumerowane od 0 do %s" %(wierzchołki-1))

macierz = {}
for i in range(wierzchołki):
    macierz[i] = []
    for k in range(wierzchołki):
        if i != k:
            if k in macierz.keys():
                macierz[i].append(macierz[k][i])
            else:
                sąsiedztwo = int(input("wpisz 0 lub 1 w zależności czy wierzchołek %s jest połączony z wierzchołkiem %s: " %(i,k)))
                macierz[i].append(sąsiedztwo)
        else:
            macierz[i].append(0)
        print("macierz sąsiedztwa: ")
        print(macierz)
def stopien_wierzcholkow(dict):
    lista = []
    for key in dict:
        lista.append(sum(dict[key]))
    return lista

def stopien_grafu(l):
    return max(l)
l = stopien_wierzcholkow(macierz)
print("stopień wierzchołków: ")
print(l)
print("stopień grafu: %d" % stopien_grafu(l))






