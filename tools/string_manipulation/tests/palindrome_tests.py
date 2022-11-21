import unittest
from is_palindrome import is_palindrome


class PalindromeTest(unittest.TestCase):
    def test_ints(self):
        # Each test should be performed with an even and odd val length
        self.assertFalse(is_palindrome(1000), msg="Int Test #1")
        self.assertFalse(is_palindrome(100), msg="Int Test #1a")

        self.assertTrue(is_palindrome(1001), msg="Int Test #2")
        self.assertTrue(is_palindrome(101), msg="Int Test #2a")

    def test_examples(self):
        # Each test should be performed with an even and odd val length
        self.assertTrue(is_palindrome("tacocat"), msg="String Test #1")
        self.assertTrue(is_palindrome("redder"), msg="String Test #1a")

        self.assertFalse(is_palindrome("hello"), msg="String Test #2")
        self.assertFalse(is_palindrome("free"), msg="String Test #2a")


if __name__ == '__main__':
    unittest.main()
