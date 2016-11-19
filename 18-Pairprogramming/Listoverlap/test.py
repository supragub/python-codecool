import unittest
from listoverlap_module import listoverlap


# Here's our "unit tests".


class ListOverlapTestCase(unittest.TestCase):
    def test_listoverlap(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        c = [1, 2, 3, 5, 8, 13]
        self.assertEqual(listoverlap(a, b), c)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
