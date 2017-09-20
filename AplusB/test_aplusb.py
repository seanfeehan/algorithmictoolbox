from unittest import TestCase
from AplusB import AplusB


class TestAplusB(TestCase):


    def test_add_numbers1(self):
        retval = AplusB.add_numbers(self, 1, 2)
        self.assertEqual(retval, 3)

    def test_add_numbers2(self):
        retval = AplusB.add_numbers(self, 44, 55)
        self.assertEqual(retval, 99)

    def test_connor_mcdavid(self):
        retval = AplusB.add_numbers(self, 44, 53)
        self.assertEqual(retval, 97)