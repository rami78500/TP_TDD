import unittest
from FizzBuzz import *

class Test_FizzBuzz(unittest.TestCase):

    def setUp(self) :
        self.instance=FizzBuzz()

    def test_affiche_sans_param(self):
        self.assertEqual(self.instance.affiche(), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")