
#!/bin/bash
#Poni�ej w zmiennej COMMAND WPISA� POLECENIE, kt�re uruchamia program!!!
#COMMAND="./a.out" #Odpalanie programu w przypadku j�zyka ANSI C
#POZOSTA�EJ CZʌCI SKRYPTU NIE ZMIENIA�!!!
COMMAND="python zad2.py"
echo "Jaki jest typ danych (1 - macierz s�siedztwa, 2 - lista s�siedztwa, 3 - lista kraw�dzi)"
read answer
if ! [[ "$answer" =~ ^[0-9]+$ ]]; then
  echo "Wprowadzi�e� nieprawid�ow� odpowied� - nie liczb�"
  exit 1
fi
if [[ "$answer" == 1 ]]; then
  echo "Uruchamiam testy dla macierzy s�siedztwa"
  listOfFiles=`ls DaneBipartite/adjMatrix | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < DaneBipartite/adjMatrix/$testFile
  done
elif [[ "$answer" == 2 ]]; then
  echo "Uruchamiam testy dla list kraw�dzi"
  listOfFiles=`ls DaneBipartite/adjList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < DaneBipartite/adjList/$testFile
  done
elif [[ "$answer" == 3 ]]; then
  echo "Uruchamiam testy dla list kraw�dzi"
  listOfFiles=`ls edgeList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND edgeList/$testFile
  done
else
  echo "Nieprawid�owa liczba"
  exit 1
fi


exit 0