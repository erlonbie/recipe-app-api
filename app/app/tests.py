"""
Sample test for the app module.
"""

from django.test import SimpleTestCase
from app.calc import add, subtract
# from app.app import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module.
    """

    def test_add_numbers(self):
        """
        Test adding two numbers together.
        """

        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Test subtracting two numbers.
        """

        res = subtract(10, 5)

        self.assertEqual(res, 5)
