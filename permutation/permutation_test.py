from unittest import TestCase
from permutation import testInclusion

class PermutationStringTest(TestCase):
    def test_permutation_ab_eidbaooo(self):
      assert testInclusion('ab', 'eidabaoo') == True
   
    def test_permutation_ab_eidboaoo(self):
      assert testInclusion('ab','eidboaoo') == False

    def test_permutation_prosperity_properties(self):
      assert testInclusion('prosperity','properties') == False
