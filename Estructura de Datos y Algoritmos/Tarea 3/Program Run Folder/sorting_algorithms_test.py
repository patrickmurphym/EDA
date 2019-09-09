import unittest
import Tarea3
from random import randint, random

class InsertionSort(unittest.TestCase):

    def test_arreglo_vacio(self):
        A = []
        self.assertEqual([], Tarea3.InsertionSort(A,True))

    def test_arreglo_desordenado(self):
        A = [randint(0,67) for x in range(100)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.InsertionSort(A,asc), sorted(C, reverse=not asc))

    def test_arreglo_ordenado(self):
        A = [x for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.InsertionSort(A,not asc), sorted(C, reverse=asc))

    def test_arreglo_unico(self):
        A = [7 for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.InsertionSort(A,not asc), sorted(C, reverse=asc))

class SelectionSort(unittest.TestCase):

    def test_arreglo_vacio(self):
        A = []
        self.assertEqual([], Tarea3.SelectionSort(A,True))

    def test_arreglo_desordenado(self):
        A = [randint(0,15) for x in range(100)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.SelectionSort(A,asc), sorted(C, reverse=not asc))

    def test_arreglo_ordenado(self):
        A = [x for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.SelectionSort(A,not asc), sorted(C, reverse= asc))

    def test_arreglo_unico(self):
        A = [7 for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.SelectionSort(A,not asc), sorted(C, reverse=asc))

class CountingSort(unittest.TestCase):

    def test_arreglo_vacio(self):
        A = []
        self.assertEqual([], Tarea3.CountingSort(A,100,False))

    def test_arreglo_desordenado(self):
        A = [randint(0,85) for x in range(142)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.CountingSort(A, 85,asc), sorted(C, reverse= not asc))

    def test_arreglo_ordenado(self):
        A = [x for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.CountingSort(A, 1000, asc), sorted(C, reverse= not asc))

    def test_arreglo_unico(self):
        A = [7 for x in range(1000)]
        C = A.copy()
        asc = random() < 0.5
        self.assertEqual(Tarea3.CountingSort(A,7, asc), sorted(C, reverse= not asc))

if __name__ == '__main__':
    unittest.main()
