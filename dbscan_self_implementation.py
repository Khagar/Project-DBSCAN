from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from pylab import *


def distance(M, p, q):
    """
    Funkcja oblicza dystans miedzy dwoma danymi punktami p i q pobierajac wspolrzedne tych punktow z macierzy M

    :param M: Macierz odleglosci miedzy punktami
    :param p: Pierwszy punkt
    :param q: Drugi punkt

    :return: dystans miedzy dwoma punktami
    """

    return (math.sqrt(math.pow(M[p, 0] - M[q, 0],2)  + math.pow(M[p, 1] - M[q, 1],2)))  # obliczanie dystansu miedzy punktami


def eps_neighborhood(M, p, q, eps):
    """
    Funkcja sprawdza czy dystans miedzy wybranymi punktami jest mniejszy od podanej liczby eps

    :param M: Macierz odleglosci miedzy punktami
    :param p: Pierwszy punkt
    :param q: drugi punkt
    :param eps: maksymalny zasieg sasiedztwa

    :return True: w przypadku gdy dystans jest mniejszy do eps
    :return False: w przypadku gdy dystans jest wiekszy od eps
    """
    if distance(M, p, q) == 0:  # zwraca false przy dystansie miedzy jednakowymi punktami np 1 i 1
        return False
    return distance(M, p, q) < eps  # jesli dystans miedzy punktami jest mniejszy niz eps to zwraca true


def cluster(M, point, eps):  # zwraca punkty dla ktorych dystans z punktu point jest mniejszy od eps

    """
    Funkcja zwraca tablice z wszystkimi punktami i ktore znajduja sie w sasiedztwie punktu point

    :param M: Macierz odleglosci miedzy punktami
    :param point: punkt dla ktorego szukamy punktow w sasiedztwie
    :param eps: maksymalny zasieg sasiedztwa
    :return seeds: zwraca tablice seeds z punktami znajdujacymi sie w sasiedztwie punktu point
    """
    seeds = []
    for i in range(0, M.shape[0]):
        if eps_neighborhood(M, point, i, eps):
            seeds.append(i)
    return seeds


def DBSCAN(M, eps, min_points):
    """
    Funkcja uzywajac algorytmu DBSCAN przedstawia na wykresie wszystkie stworzone clustery

    :param M: Macierz odleglosci miedzy punktami
    :param eps: maksymalny zasieg sasiedztwa
    :param min_points: Minimalna liczba punktow aby dany punkt byl CORE punktem

    :return: Zwraca wykres przedstawiajacy wszystkie stworzone clustery. Punkty nie nalezace do zadnego z clusterow sa zaznaczone na czarno, BORDER punkty sa zaznaczone malym zakolorowanym kolem natomiast CORE punkty duzym zakolorwanym kolem
    """
    colors = ['r', 'g', 'b', 'y', 'c', 'm']  # tablica kolorow - inny kolor dla kazdego clustera
    checked = np.zeros(M.shape[
                           0])  # tablica sprawdzonych punktow wypelniona zerami jesli punkt zostal sprawdzony zmieniana jest wartosc na 1print(checked)
    classification = np.empty(M.shape[0])
    classification.fill(0)
    cluster_count = 0
    for i in range(0, len(colors)):  # for odpowiedzialny do tworzenia clusterow (kazdy cluster inny kolor)
        for j in range(0, len(checked)):  # szukanie pierwszego niesprawdzonego punktu
            if checked[j] != 1:
                seeds = cluster(M, j, eps)
                startpoint = j
                if min_points > len(seeds):
                    checked[
                        startpoint] = 1  # jesli punkt ma mniej sasiadow niz minimalna liczba to ustawia punkt jako sprawdzony i nic z nim dalej nie robi bo jest do dupy

                if min_points <= len(seeds):
                    plt.plot(M[startpoint, 0], M[startpoint, 1], 'k.', markeredgecolor='k', markerfacecolor=colors[i],
                             markersize=np.pi * 3 ** 2)  # jesli ma minimalna liczbe sasiadow to robi koleczko na wykresie
                    checked[startpoint] = 1
                    classification[startpoint] = i + 1
                    break  # jesli znaleziono niesprawdzony punkt wychodzi z petli
        while len(seeds) > 0:

            point = seeds[0]  # wybranie za kolejny punkt pierwszego punktu z tablicy seeds
            results = cluster(M, point, eps)  # zapisanie punktow ktore spelniaja warunek z neighborhood
            if checked[point] != 1:
                if min_points > len(results) and (classification[point] == 0 or classification[point] == -1):
                    checked[
                        point] = 1  # jesli punkt ma mniej sasiadow niz minimalna liczba to ustawia punkt jako sprawdzony i ustala go jako border
                    plt.plot(M[point, 0], M[point, 1], 'k.', markeredgecolor='k', markerfacecolor=colors[i],
                             markersize=8)
                    classification[point] = -(i + 1)
                if min_points <= len(results):
                    plt.plot(M[point, 0], M[point, 1], 'k.', markeredgecolor='k', markerfacecolor=colors[i],
                             markersize=np.pi * 3 ** 2)  # jesli ma minimalna liczbe sasiadow to robi koleczko na wykresie
                    checked[point] = 1
                    classification[point] = i + 1
                    for k in range(0, len(results)):
                        result_point = results[k]
                        seeds.append(
                            result_point)  # dodanie do tablicy seeds punktow ktore znajdowaly sie w sasiedztwie punktu point
            seeds.remove(seeds[0])  # usuwa juz sprawdzony element z tablicy seeds
        if np.sum(checked) == M.shape[
            0]:  # jesli juz wszystkie punkty zostaly sprawdzone to wychodzi z petli - po tym wszystkie clustery powinny byc zrobione
            break
    return plt.show()

# Generowanie przykladowego ukladu wspolrzednych
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)
X = StandardScaler().fit_transform(X)


x, y = zip(*X)
plt.scatter(x, y, s=5, color='black')

DBSCAN(X,0.3,10)