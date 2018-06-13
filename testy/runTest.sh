
#!/bin/bash
#Poni¿ej w zmiennej COMMAND WPISAÆ POLECENIE, które uruchamia program!!!
#COMMAND="./a.out" #Odpalanie programu w przypadku jêzyka ANSI C
#POZOSTA£EJ CZÊŒCI SKRYPTU NIE ZMIENIAÆ!!!
COMMAND="python zad2.py"
echo "Jaki jest typ danych (1 - macierz s¹siedztwa, 2 - lista s¹siedztwa, 3 - lista krawêdzi)"
read answer
if ! [[ "$answer" =~ ^[0-9]+$ ]]; then
  echo "Wprowadzi³eœ nieprawid³ow¹ odpowiedŸ - nie liczbê"
  exit 1
fi
if [[ "$answer" == 1 ]]; then
  echo "Uruchamiam testy dla macierzy s¹siedztwa"
  listOfFiles=`ls DaneBipartite/adjMatrix | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < DaneBipartite/adjMatrix/$testFile
  done
elif [[ "$answer" == 2 ]]; then
  echo "Uruchamiam testy dla list krawêdzi"
  listOfFiles=`ls DaneBipartite/adjList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < DaneBipartite/adjList/$testFile
  done
elif [[ "$answer" == 3 ]]; then
  echo "Uruchamiam testy dla list krawêdzi"
  listOfFiles=`ls edgeList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND edgeList/$testFile
  done
else
  echo "Nieprawid³owa liczba"
  exit 1
fi


exit 0