#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class FirstTestClass(unittest.TestCase):
    def test_add(self):
        self.assertEquals(120, 100 + 20)


class SecondTestClass(unittest.TestCase):
    def setUp(self):
        self.val = 210

    def test_sub(self):
        self.assertEquals(210, self.val)
        self.val = self.val - 40
        self.assertEquals(170, self.val)

    def test_mul(self):
        self.assertEquals(420, self.val * 2)


if __name__ == '__main__':
    unittest.main()
