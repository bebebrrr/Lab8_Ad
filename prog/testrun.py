#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import testind


if __name__ == "__main__":
    ind_test_suite = unittest.TestSuite()
    ind_test_suite.addTest(unittest.makeSuite(testind.indTest))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(ind_test_suite)
