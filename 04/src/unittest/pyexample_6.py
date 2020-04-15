#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pyexample_6_module_a
import pyexample_6_module_b


loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(pyexample_6_module_a)
suite.addTests(loader.loadTestsFromModule(pyexample_6_module_b))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
