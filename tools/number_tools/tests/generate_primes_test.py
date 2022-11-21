import unittest
from tools.number_tools.generate_primes import generate_primes_until


class GeneratePrimesTest(unittest.TestCase):
    def test_generation(self):
        # Define an expected list with a max_num of 120
        expected_list = [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                         53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

        # Check expected list equal to the result of 120
        self.assertEqual(generate_primes_until(120), expected_list)


if __name__ == '__main__':
    unittest.main()
