#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class BaseTestClass(unittest.TestCase):
    def test_base_1(self):
        self.assertEquals(210, 110 * 2 - 10)

    def test_base_2(self):
        self.assertTrue(False is not None)


class DerivedTestClassA(BaseTestClass):
    def test_derived_a(self):
        self.assertEquals(100, 10 * 10)


class DerivedTestClassB(BaseTestClass):
    def test_derived_b(self):
        self.assertEquals(45, 46 - 1)


if __name__ == '__main__':
    unittest.main()
