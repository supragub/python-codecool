import unittest
from years_module import years


# Here's our "unit tests".


class YearsTestCase(unittest.TestCase):
    def test_100years(self):
        self.assertEqual(years(35), 2081)
        self.assertEqual(years(2), 2114)
        self.assertEqual(years(99), 2017)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
