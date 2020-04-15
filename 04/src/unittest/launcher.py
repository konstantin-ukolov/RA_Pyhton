#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

loader = unittest.TestLoader()

suite = loader.discover(start_dir='.', pattern='pyexample_*.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
