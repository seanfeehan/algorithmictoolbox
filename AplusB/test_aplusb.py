from unittest import TestCase
from AplusB import AplusB


class TestAplusB(TestCase):

    def test_add1(self):
        retval = AplusB.add_numbers(1, 2)
        self.assertEquals(retval, 3)

    def test_add_numbers(self):
        self.fail()
