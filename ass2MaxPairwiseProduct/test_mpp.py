from unittest import TestCase
from mpp import mpp

class TestMpp(TestCase):
    def test_maxPairwiseProduct(self):
        retval = mpp.maxPairwiseProduct(self, 3, [1,2,3])
        self.assertEqual(retval, 6)
