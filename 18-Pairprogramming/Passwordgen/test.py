import unittest
from passwordgen_module import passwordgen


# Here's our "unit tests".


class PasswordgenTestCase(unittest.TestCase):
    def test_passwordgen(self):
        result = passwordgen()
        self.assertRegex(result, r"[a-z]")
        self.assertRegex(result, r"[A-Z]")
        self.assertRegex(result, r"[0-9]")
        self.assertRegex(result, r"[!@#$%^&*()?]")
        self.assertGreaterEqual(len(result), 8)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
