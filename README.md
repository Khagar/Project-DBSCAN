# Project-DBSCAN

## Opis projektu oraz podział obowiązków

Naszym zadaniem była własna implementacja algorytmu DBSCAN oraz porównanie jej z implementacja dostępną w scikit-learnie.

### Podział obowiązków:

Karol Jasina - PM, Implementacja algorytmu oraz stworzenie dokumentacji

Maciej Tabor - Implementacja algorytmu

Miłosz Munik - Testy jednostkowe

## Uruchomienie algorytmu

  DBSCAN(M, eps, min_points)
  M - macierz współrzędnych w postaci M[x y]
  eps - maksymalny zasięg sąsiedztwa
  min_points - minimalna liczba punktów znajdujących się w sąsiedztwie

## Porównanie wyników

### Przykładowy zbiór współrzędnych dla którego porównane zostały wyniki algorytmów:

![screenshot](http://i.imgur.com/ODt4RDY.png)

### Układ współrzędnych uzyskany za pomocą DBSCAN zaimplementowanego przez nas:

![screenshot](http://i.imgur.com/uEKvR6x.png)

### Układ współrzędnych uzyskany za pomocą DBSCAN z scikit-learn:

![screenshot](http://i.imgur.com/om3PNk6.png)

	
## Dokumentacja

dbscan_self_implementation.distance(M, p, q)
Funkcja oblicza dystans miedzy dwoma danymi punktami p i q pobierajac wspolrzedne tych punktow z macierzy M

Parameters:	
M – Macierz odleglosci miedzy punktami
p – Pierwszy punkt
q – Drugi punkt
Returns:	
dystans miedzy dwoma punktami

-----------------------------------------------------------------------------------------------------

dbscan_self_implementation.eps_neighborhood(M, p, q, eps)
Funkcja sprawdza czy dystans miedzy wybranymi punktami jest mniejszy od podanej liczby eps

Parameters:	
M – Macierz odleglosci miedzy punktami
p – Pierwszy punkt
q – drugi punkt
eps – maksymalny zasieg sasiedztwa
Return True:	
w przypadku gdy dystans jest mniejszy do eps
Return False:	
w przypadku gdy dystans jest wiekszy od eps

-----------------------------------------------------------------------------------------------------

dbscan_self_implementation.cluster(M, point, eps)
Funkcja zwraca tablice z wszystkimi punktami i ktore znajduja sie w sasiedztwie punktu point

Parameters:	
M – Macierz odleglosci miedzy punktami__
point – punkt dla ktorego szukamy punktow w sasiedztwie__
eps – maksymalny zasieg sasiedztwa__
Return seeds:	
zwraca tablice seeds z punktami znajdujacymi sie w sasiedztwie punktu point__

-----------------------------------------------------------------------------------------------------

dbscan_self_implementation.DBSCAN(M, eps, min_points)

Funkcja uzywajac algorytmu DBSCAN przedstawia na wykresie wszystkie stworzone clustery

Parameters:	
M – Macierz odleglosci miedzy punktami__
eps – maksymalny zasieg sasiedztwa__
min_points – Minimalna liczba punktow aby dany punkt byl CORE punktem__
Returns:	
Zwraca wykres przedstawiajacy wszystkie stworzone clustery. Punkty nie nalezace do zadnego z clusterow sa zaznaczone na czarno, BORDER punkty sa zaznaczone malym zakolorowanym kolem natomiast CORE punkty duzym zakolorwanym kolem

