#coding:utf-8
from calculator import Count
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        print("Test Case Start!")
    #
    # def test_add(self):
    #     j = Count(2,3)
    #     self.assertEqual(j.add(),5)
    # def test_add2(self):
    #     j = Count(5,5)
    #     self.assertEqual(j.add(),10)
    # def test_sub(self):
    #     j = Count(1,2)
    #     self.assertEqual(j.sub(),-1)
    # def test_sub2(self):
    #     j = Count(99,88)
    #     self.assertEqual(j.sub(),11)

    def tearDown(self):
        print("Test Case End!")

class TestAdd(Mytest):

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(5,5)
        self.assertEqual(j.add(),10)

class TestSub(Mytest):

    def test_sub(self):
        j = Count(1,2)
        self.assertEqual(j.sub(),-1)
    def test_sub2(self):
        j = Count(99,88)
        self.assertEqual(j.sub(),11)

if __name__=='__main__':
    unittest.main()