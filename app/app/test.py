"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_two_numbers(self):
        """Test case for adding two numbers"""
        res = calc.sum(5, 6)
        self.assertEqual(res, 11)
