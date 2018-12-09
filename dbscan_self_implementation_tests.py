import unittest
import numpy as np


def _distance(M,p,q):
    return np.math.sqrt(np.math.pow((M[p,0]-M[q,0]),2)+np.math.pow((M[p,1]-M[q,1]),2)) #obliczanie dystansu miedzy punktami

def _eps_neighborhood(M,p,q,eps):
    if _distance(M,p,q)==0: #zwraca false przy dystansie miedzy jednakowymi punktami np 1 i 1
         return False
    return _distance(M,p,q) < eps #jesli dystans miedzy punktami jest mniejszy niz eps to zwraca true

def _cluster(M,point,eps): #zwraca punkty dla ktorych dystans z punktu point jest mniejszy od eps
    seeds=[]
    for i in range(0, M.shape[0]):
        if _eps_neighborhood(M,point,i,eps):
            seeds.append(i)
    return seeds


class TestDBSCANMethods(unittest.TestCase):
    """
    Przetestowanie funkcji uzytych w algorytmie DBSCAN. Sam algorytm DBSCAN nie zostaje przetestowany poniewaz zwraca on wykres ze stworzonymi clusterami.
    Porownanie algorytmu DBSCAN stworzonego przez nas z algorytmem DBSCAN w bibliotece scikit-learn zostanie przeprowadzone graficznie.
    """
    def test_distance(self):
        test = _distance(np.matrix('1 1;4 5'), 0, 1)
        self.assertEquals(test, 5, 'Blad')

    def test_eps_neighborhood(self):
        test2 = _eps_neighborhood(np.matrix('1 1;4 5'), 0, 1, 6)
        test3 = _eps_neighborhood(np.matrix('1 1;4 5'), 0, 1, 3)
        self.assertTrue(test2)

        self.assertFalse(test3)

    def test_cluster(self):
        test4 = _cluster(np.matrix('1 1 ; 4 5 ; 2 2; 3 3'), 2, 20)
        test5 = _cluster(np.matrix('1 1 ; 4 5 ; 2 2; 3 3'), 2, 3)
        example = [0, 1, 3]
        self.assertListEqual(test4, example, 'Blad')


if __name__ == '__main__':
    unittest.main()