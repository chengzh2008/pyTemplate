# -*- coding: utf-8 -*-

import unittest

from src import lib2 as L2


class Lib2TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert L2.get_str2() == "str2"

if __name__ == '__main__':
    unittest.main()
