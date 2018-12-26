import unittest
from mathlib_kkotari import functions

class TestFun(unittest.TestCase):
    def test_add1(self):
        assert functions.add(1,2,3) == 6

    def test_add2(self):
        assert functions.add(3, 4) == 7

    def test_mul(self):
        assert functions.mul(2,3) == 6
