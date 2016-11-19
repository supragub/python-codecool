import unittest
from palindrome_module import palindrome


# Here's our "unit tests".


class PalindromeTestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome("Anna"), True)
        self.assertEqual(palindrome("A nut for a jar of tuna"), True)
        self.assertEqual(palindrome("Tom Hanks"), False)
        self.assertEqual(palindrome("T"), True)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
