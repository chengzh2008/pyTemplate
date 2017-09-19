# -*- coding: utf-8 -*-

import unittest

from src import lib1 as L1


class Lib1TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert L1.get_1() == 2

if __name__ == '__main__':
    unittest.main()
