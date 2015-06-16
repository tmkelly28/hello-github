"""test_basic_statistics.py
"""

import unittest
from basic_statistics import calculateFormulas

class TestBasicStatistics(unittest.TestCase):

	def test_happy_path(self):
		file = ['2', '4', '4', '4', '5', '5', '7', '9']
		mean, variance, standard_deviation = calculateFormulas(file)
		self.assertEqual(mean, 5)
		self.assertEqual(variance, 4)
		self.assertEqual(standard_deviation, 2.0)

if __name__ == '__main__':
	unittest.main()