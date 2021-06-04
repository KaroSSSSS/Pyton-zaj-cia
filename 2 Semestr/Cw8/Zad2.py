import unittest
from ppm import BmrCalculator
class TestPPM(unittest.TestCase):
    def setUp(self) -> None:
        self.bmr = BmrCalculator()
    def test_if_cal_are_more_than_0_for_men_ppm(self):
        bmr_check = self.bmr.men_ppm(12,23,12)
        self.assertTrue(bmr_check>0)
if __name__ == '__main__':
    unittest.main()