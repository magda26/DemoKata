from unittest import TestCase
from Calculator import Calculator

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "Empty string")

    def test_add_oneString(self):
        self.assertEqual(Calculator().add("1"), 1, "A number")

    def test_add_stringWithANumber(self):
        self.assertEqual(Calculator().add("1"), 1, "A number")
        self.assertEqual(Calculator().add("2"), 2, "A number")

    def test_add_stringWithTwoNumbers(self):
        self.assertEqual(Calculator().add("1,3"), 4, "Two numbers")

    def test_add_stringWithManyNumbers(self):
        self.assertEqual(Calculator().add("1,3,4"), 8, "Multiple numbers")

    def test_add_stringWithManyNumbersAndSeparators(self):
        self.assertEqual(Calculator().add("1#3/4:4-1"), 13, "Multiple numbers with different separators")







