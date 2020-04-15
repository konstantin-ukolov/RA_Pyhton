#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def setUpModule():
    print('In setUpModule()')


def tearDownModule():
    print('In tearDownModule()')


class FirstTestClass(unittest.TestCase):
    '''
    Invoked without setUp and tearDown methods
    '''
    def test_add(self):
        print('In test_add()')
        self.assertEquals(120, 100 + 20)


class SecondTestClass(unittest.TestCase):
    '''
    Invoked with setUpClass/setUp and tearDown/tearDownClass methods
    '''
    @staticmethod
    def setUpClass():
        print('In setUpClass()')

    def setUp(self):
        print('In setUp()')

    def test_sub(self):
        print('In test_sub()')

        self.assertEquals(210, 110 * 2 - 10)
        self.assertEquals(170, 140 - (-30))

    def test_mul(self):
        print('In test_mul()')

        self.assertEquals(420, 210 * 2)
        self.assertEquals(420, 210 * 2.0000000000000000000001)

    def tearDown(self):
        print('In tearDown()')

    @staticmethod
    def tearDownClass():
        print('In tearDownClass()')


if __name__ == '__main__':
    unittest.main()
