from unittest import TestCase
from palindrome import is_palindrome

class PalindromeTest(TestCase):
    def test_is_palindrome_racecar(self):
      assert is_palindrome('racecar') == True

    def test_is_palindrome_amana(self):
      assert is_palindrome('A man, a plan, a canal: Panama') == True

    def test_is_palindrome_malayalam(self):
      assert is_palindrome('malayalam') == True

    def test_is_palindrome_raceacar(self):
      assert is_palindrome('race a car') == False
