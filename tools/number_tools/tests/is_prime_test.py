import unittest
from tools.number_tools.is_prime import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))

    def test_composites(self):
        self.assertFalse(is_prime(1000))
        self.assertFalse(is_prime(100000))
        self.assertFalse(is_prime(202))


if __name__ == '__main__':
    unittest.main()
