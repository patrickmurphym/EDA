import unittest
import Tarea4
from random import randint, random

hash_len = 1000
class HashFunction(unittest.TestCase):

    def test_hashing_controlled(self):
        self.assertEqual(1, Tarea4.f_hash(1,2,3,5))

    def test_hashing_a_equals_0(self):
        c = randint(0,10000)
        a = 0
        m = randint(1,1000)
        x = randint(1,100000)
        self.assertEqual(c%m, Tarea4.f_hash(a,c,m,x))

    def test_hashing_random_numbers(self):
        a = randint(1,7)
        c = randint(0,134)
        x = randint(0,120)
        self.assertEqual((a*x)+c, Tarea4.f_hash(a,c,hash_len,x))

class InsertNumber(unittest.TestCase):

    def test_insert_empty(self):
        Tarea4.c = randint(1,1000)
        Tarea4.a = randint(1,1000)
        hash_table = [-1] * 1000
        self.assertEqual(1, Tarea4.insertar(hash_table, hash_len, randint(1,1000)))
    
    def test_insert_data(self):
        Tarea4.c = 33
        Tarea4.a = 55
        hash_table = [-1] * hash_len
        for i in range(500):
            hash_table[randint(0,hash_len-1)] = 1
        hash_table[153] = -1
        self.assertEqual(1, Tarea4.insertar(hash_table, hash_len, 3984))

    def test_insert_last_position(self):
        Tarea4.c = 10
        Tarea4.a = 10
        hash_table = [-1] * 1000
        hash_table[100] = 1
        self.assertEqual(0, Tarea4.insertar(hash_table, 101, 9))

    def test_insert_correction(self):
        Tarea4.c = 343402
        Tarea4.a = 600482
        hash_table = [-1] * hash_len
        hash_table[402] = 1
        for i in range(890):
            hash_table[randint(0,hash_len-1)] = 1
        hash_table[900] = -1
        self.assertEqual(2, Tarea4.insertar(hash_table, hash_len, 3000000))

class FindNumber(unittest.TestCase):

    def test_find_number_in_hash(self):
        Tarea4.c = 2
        Tarea4.a = 6000002
        hash_table = [-1] * hash_len
        hash_table[866] = 78432
        self.assertEqual(1, Tarea4.buscar(hash_table, hash_len, 78432))

    def test_find_number_not_in_hash(self):
        Tarea4.c = 654321
        Tarea4.a = 123456
        hash_table = [-1] * hash_len
        self.assertEqual(0, Tarea4.buscar(hash_table, hash_len, 61235))

    def test_find_number_corrected(self):
        Tarea4.c = 846854
        Tarea4.a = 194884184
        hash_table = [-1] * hash_len
        for i in range(890):
            hash_table[randint(0,hash_len-1)] = 1
        hash_table[14] = 145381
        self.assertEqual(1, Tarea4.buscar(hash_table, 39, 145381))

class EliminateNumber(unittest.TestCase):

    def test_eliminate_number_in_hash(self):
        Tarea4.c = 2
        Tarea4.a = 6000002
        hash_table = [-1] * hash_len
        hash_table[866] = 78432
        self.assertEqual(1, Tarea4.eliminar(hash_table, hash_len, 78432))
    
    def test_eliminate_number_not_in_hash(self):
        Tarea4.c = 6543211
        Tarea4.a = 1234562
        hash_table = [-1] * hash_len
        self.assertEqual(0, Tarea4.eliminar(hash_table, hash_len, 61235))

    def test_eliminate_number_corrected(self):
        Tarea4.c = 84685486
        Tarea4.a = 191214
        hash_table = [-1] * hash_len
        for i in range(890):
            hash_table[randint(0,hash_len-1)] = 1
        hash_table[990] = 145381
        self.assertEqual(1, Tarea4.buscar(hash_table, hash_len, 145381))

class FC(unittest.TestCase):

    def test_FC_empty(self):
        hash_table = [-1] * hash_len
        self.assertEqual(0, Tarea4.FC(hash_table, hash_len))
    
    def test_FC_full(self):
        hash_table = [1] * hash_len
        self.assertEqual(1, Tarea4.FC(hash_table, hash_len))
    
    def test_FC_random(self):
        m = randint(50,999)
        n = randint(1,m)
        hash_table = [-1] * hash_len
        for i in range(n):
            hash_table[i] = 1
        self.assertEqual(n/m, Tarea4.FC(hash_table, m))

if __name__ == '__main__':
    unittest.main()
