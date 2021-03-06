﻿#This file was originally generated by PyScripter's unitest wizard

import unittest
from ddt import data, unpack, ddt
import sys

sys.path.append("..\\")

from fuzzycalc.tnorm import *

@ddt
class TestMinMax(unittest.TestCase):

    def setUp(self):
        self.norm = MinMax()

    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0.2, 0.5, 0.2),
        (0.2, 0.2, 0.5),
    )
    @unpack
    def test_norm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))

    @data(
        (0, 0, 0),
        (1, 0, 1),
        (1, 1, 0.5),
        (1, 1, 1),
        (0.5, 0, 0.5),
        (0.5, 0.5, 0.2),
        (0.5, 0.2, 0.5),
    )
    @unpack
    def test_conorm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.conorm(val1, val2))

@ddt
class TestSumProd(unittest.TestCase):

    def setUp(self):
        self.norm = SumProd()

    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0.1, 0.5, 0.2),
        (0.1, 0.2, 0.5),
    )
    @unpack
    def test_norm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))


    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0.1, 0.5, 0.2),
        (0.1, 0.2, 0.5),
    )
    @unpack
    def test_conorm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))

@ddt
class TestMargin(unittest.TestCase):

    def setUp(self):
        self.norm = Margin()

    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0, 0.5, 0.2),
        (0, 0.2, 0.5),
    )
    @unpack
    def test_norm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))


    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0, 0.5, 0.2),
        (0, 0.2, 0.5),
    )
    @unpack
    def test_conorm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))

@ddt
class TestDrastic(unittest.TestCase):

    def setUp(self):
        self.norm = Drastic()

    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0, 0.5, 0.2),
        (0, 0.2, 0.5),
    )
    @unpack
    def test_norm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))


    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0, 0.5, 0.2),
        (0, 0.2, 0.5),
    )
    @unpack
    def test_conorm(self, expected, val1, val2):
        self.assertEqual(expected, self.norm.norm(val1, val2))

@ddt
class TestTnorm1(unittest.TestCase):

    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0.1, 0.5, 0.2),
        (0.1, 0.2, 0.5),
    )
    @unpack
    def test_norm(self, expected, val1, val2):
        par = 1.0
        self.norm = Tnorm1(par)
        self.assertEqual(expected, self.norm.norm(val1, val2))


    @data(
        (0, 0, 0),
        (0, 0, 1),
        (0.5, 1, 0.5),
        (1, 1, 1),
        (0, 0, 0.5),
        (0.1, 0.5, 0.2),
        (0.1, 0.2, 0.5),
    )
    @unpack
    def test_conorm(self, expected, val1, val2):
        par = 1.0
        self.norm = Tnorm1(par)
        self.assertEqual(expected, self.norm.norm(val1, val2))

class TestTnorm2(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

class TestTnorm3(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

class TestTnorm4(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

class TestTnorm5(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

class TestTnorm6(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

class TestTnorm7(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testnorm(self):
        pass

    def testconorm(self):
        pass

if __name__ == '__main__':
    unittest.main()
