import unittest
from fizzbuzz_module import fizzbuzz


# Here's our "unit tests".


class FizzBuzzAcceptanceTestCase(unittest.TestCase):
    '''
    Test that fizzbuzz(int) returns int
    unless multiple of 3 (then returns 'Fizz')
           multiple of 5 (then returns 'Buzz')
           multiple of both (then returns 'FizzBuzz')
    '''
    def test_normal_numbers(self):
        '''
        test that an integer >= 0 not evenly divisible
        by three or five returns the same
        '''
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(fizzbuzz(998), 998)

    def test_fizz(self):
        '''evenly divisible by 3 returns Fizz'''
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(fizzbuzz(111), 'Fizz')
        self.assertEqual(fizzbuzz(999), 'Fizz')

    def test_buzz(self):
        '''evenly divisible by 5 returns Buzz'''
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(20), 'Buzz')
        self.assertEqual(fizzbuzz(500), 'Buzz')

    def test_fizz_buzz(self):
        '''evenly divisible by 3 and 5 returns FizzBuzz'''
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')
        self.assertEqual(fizzbuzz(600), 'FizzBuzz')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
