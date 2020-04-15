#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class BaseTestClass(unittest.TestCase):
    def test_ok(self):
        self.assertEquals(210, 110 * 2 - 10)

    @unittest.skip('not supported')
    def test_skip(self):
        self.assertEquals(1000, 10 * 10 * 10)

    def test_fail(self):
        self.assertEquals(420, 210 * 2.1)

    def test_error(self):
        raise ZeroDivisionError('Error! Divizion by zero')

    @unittest.expectedFailure
    def test_expected(self):
        raise ZeroDivisionError('Error! Divizion by zero')

    @unittest.expectedFailure
    def test_unexpected_ok(self):
        self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
